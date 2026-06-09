from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cv2
import numpy as np
import os
import uuid
import torch
from PIL import Image
import io
import matplotlib.pyplot as plt
import pandas as pd
from tempfile import NamedTemporaryFile, mkdtemp
import shutil
from typing import Optional, List, Dict, Any
import logging
import time
import requests

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("tongue-analysis-api")

# Check if CUDA is available for PyTorch
try:
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Using device: {DEVICE}")
except Exception as e:
    logger.warning(f"Could not initialize torch device: {e}")
    DEVICE = "cpu"

# Constants
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tongue Analysis API - Healthy"}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models
sam_model = None
sam_predictor = None
roboflow_client = None
SAM_AVAILABLE = False
ROBOFLOW_AVAILABLE = False
PAPILLAE_AVAILABLE = False
CRACK_DETECTION_AVAILABLE = False
JAGGED_SCORE_AVAILABLE = False
LLM_AVAILABLE = False

# Model loading functions
def load_sam_model(checkpoint_path="sam_vit_h.pth", model_type="vit_h"):
    """Load the Segment Anything Model"""
    global SAM_AVAILABLE
    try:
        if not os.path.exists(checkpoint_path):
            logger.warning(f"SAM checkpoint not found at {checkpoint_path}")
            return None, None
        
        from segment_anything import sam_model_registry, SamPredictor
        
        logger.info(f"Loading SAM model from {checkpoint_path}")
        sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
        sam.to(DEVICE)
        predictor = SamPredictor(sam)
        
        logger.info("SAM model loaded successfully")
        SAM_AVAILABLE = True
        return sam, predictor
    except ImportError:
        logger.warning("segment_anything not installed. SAM functionality disabled.")
        return None, None
    except Exception as e:
        logger.warning(f"Failed to load SAM model: {str(e)}")
        return None, None

def load_roboflow_client(api_key="UySFJBcSCBCxmwiEA9ea"):
    """Load the Roboflow client for tongue detection"""
    global ROBOFLOW_AVAILABLE
    try:
        from inference_sdk import InferenceHTTPClient
        
        logger.info("Initializing Roboflow client")
        client = InferenceHTTPClient(
            api_url="https://serverless.roboflow.com",
            api_key=api_key
        )
        
        logger.info("Roboflow client initialized successfully")
        ROBOFLOW_AVAILABLE = True
        return client
    except ImportError:
        logger.warning("inference_sdk not installed. Roboflow functionality disabled.")
        return None
    except Exception as e:
        logger.warning(f"Failed to initialize Roboflow client: {str(e)}")
        return None

def check_custom_modules():
    """Check availability of custom modules"""
    global PAPILLAE_AVAILABLE, CRACK_DETECTION_AVAILABLE, JAGGED_SCORE_AVAILABLE, LLM_AVAILABLE
    
    try:
        import tongue_papillae_analyzer
        PAPILLAE_AVAILABLE = True
        logger.info("tongue_papillae_analyzer loaded")
    except ImportError as e:
        logger.warning(f"tongue_papillae_analyzer not available: {e}")
    
    try:
        import Tongue_crack_detection_model
        CRACK_DETECTION_AVAILABLE = True
        logger.info("Tongue_crack_detection_model loaded")
    except ImportError as e:
        logger.warning(f"Tongue_crack_detection_model not available: {e}")
    
    try:
        import jaggedScore
        JAGGED_SCORE_AVAILABLE = True
        logger.info("jaggedScore loaded")
    except ImportError as e:
        logger.warning(f"jaggedScore not available: {e}")
    
    try:
        import llmcall
        LLM_AVAILABLE = True
        logger.info("llmcall loaded")
    except ImportError as e:
        logger.warning(f"llmcall not available: {e}")

@app.on_event("startup")
async def startup_event():
    """Initialize models when the server starts"""
    global sam_model, sam_predictor, roboflow_client
    
    logger.info("Server startup initiated")
    
    # Check custom modules
    check_custom_modules()
    
    # Load SAM model
    sam_model, sam_predictor = load_sam_model()
    
    # Load Roboflow client
    roboflow_client = load_roboflow_client()
    
    logger.info("Server startup complete")

def save_uploaded_file(file: UploadFile) -> str:
    """Save the uploaded file and return the file path"""
    try:
        temp_file = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}{os.path.splitext(file.filename)[1]}")
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return temp_file
    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

def read_image_file(file: UploadFile) -> np.ndarray:
    """Read image file into OpenCV format"""
    try:
        contents = file.file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        file.file.seek(0)  # Reset file pointer for potential reuse
        return img
    except Exception as e:
        logger.error(f"Error reading image: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")

def detect_tongue_roboflow(image: np.ndarray):
    """Detect tongue in the image using Roboflow or fallback"""
    if roboflow_client is None or not ROBOFLOW_AVAILABLE:
        logger.info("Roboflow not available, using image center as fallback")
        height, width = image.shape[:2]
        return np.array([[width/2, height/2]])
    
    try:
        result = roboflow_client.infer(image, model_id="tongue-93kco/3")
        
        if "predictions" in result and len(result["predictions"]) > 0:
            prediction = result["predictions"][0]
            x = prediction["x"]
            y = prediction["y"]
            logger.info(f"Detected tongue at: x={x}, y={y}")
            return np.array([[x, y]])
        else:
            logger.warning("No tongue detected by Roboflow, using fallback")
            height, width = image.shape[:2]
            return np.array([[width/2, height/2]])
    except Exception as e:
        logger.warning(f"Roboflow detection error: {str(e)}, using fallback")
        height, width = image.shape[:2]
        return np.array([[width/2, height/2]])

def segment_tongue_sam(image: np.ndarray, input_point: np.ndarray):
    """Segment the tongue using SAM or fallback to simple thresholding"""
    if sam_predictor is None or not SAM_AVAILABLE:
        logger.info("SAM not available, using simple thresholding as fallback")
        return simple_tongue_segmentation(image)
    
    try:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        sam_predictor.set_image(image_rgb)
        
        input_label = np.array([1])
        masks, _, _ = sam_predictor.predict(
            point_coords=input_point,
            point_labels=input_label,
            multimask_output=False,
        )
        
        mask = masks[0]
        segmented_image = np.zeros_like(image)
        segmented_image[mask] = image[mask]
        
        logger.info("Tongue segmentation completed with SAM")
        return segmented_image, mask
    except Exception as e:
        logger.warning(f"SAM segmentation error: {str(e)}, using fallback")
        return simple_tongue_segmentation(image)

def simple_tongue_segmentation(image: np.ndarray):
    """Fallback tongue segmentation using simple thresholding"""
    try:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_tongue = np.array([0, 30, 40])
        upper_tongue = np.array([20, 255, 255])
        
        mask = cv2.inRange(hsv, lower_tongue, upper_tongue)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        segmented_image = np.zeros_like(image)
        segmented_image[mask > 0] = image[mask > 0]
        
        logger.info("Tongue segmentation completed with simple thresholding")
        return segmented_image, mask
    except Exception as e:
        logger.error(f"Fallback segmentation error: {str(e)}")
        return image, np.ones(image.shape[:2], dtype=np.uint8) * 255

def detect_white_coating(image: np.ndarray, mask: np.ndarray) -> Dict[str, Any]:
    """Detect white coating on the tongue"""
    try:
        mask = mask.astype(np.uint8) * 255 if mask.dtype != np.uint8 else mask
        
        masked_image = cv2.bitwise_and(image, image, mask=mask)
        hsv = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)
        
        lower_white = np.array([0, 0, 180])
        upper_white = np.array([180, 80, 255])
        
        white_mask = cv2.inRange(hsv, lower_white, upper_white)
        contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        coating_visualization = image.copy()
        cv2.drawContours(coating_visualization, contours, -1, (0, 255, 0), 2)
        
        white_pixels = cv2.countNonZero(white_mask)
        tongue_pixels = cv2.countNonZero(mask)
        white_percent = (white_pixels / tongue_pixels) * 100 if tongue_pixels > 0 else 0
        
        logger.info(f"White coating detection completed: {white_percent:.2f}%")
        
        coating_viz_path = os.path.join(OUTPUT_DIR, f"coating_{uuid.uuid4()}.jpg")
        cv2.imwrite(coating_viz_path, coating_visualization)
        
        return {
            "white_coating_percentage": white_percent,
            "visualization_path": coating_viz_path
        }
    except Exception as e:
        logger.error(f"Error in white coating detection: {str(e)}")
        return {
            "white_coating_percentage": 0,
            "visualization_path": ""
        }

def analyze_papillae(image_path: str) -> Dict[str, Any]:
    """Analyze papillae in the tongue image"""
    if not PAPILLAE_AVAILABLE:
        logger.warning("Papillae analyzer not available, returning default values")
        return {
            "total_papillae": 0,
            "avg_size": 0.0,
            "avg_redness": 0.0,
        }
    
    try:
        from tongue_papillae_analyzer import TonguePapillaeAnalyzer
        
        analyzer = TonguePapillaeAnalyzer(
            patch_size=64, 
            threshold_adjust=1.2,
            min_papillae_size=15,
            max_papillae_size=400
        )
        
        results_df, visualization_image, segmentation_viz, patch_viz = analyzer.analyze_image(image_path)
        report = analyzer.generate_report(results_df)
        
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        visualization = analyzer.visualize_results(image, results_df)
        
        viz_path = os.path.join(OUTPUT_DIR, f"papillae_{uuid.uuid4()}.jpg")
        plt.figure(figsize=(18, 12))
        
        plt.subplot(2, 2, 1)
        plt.title("Original Image")
        plt.imshow(image)
        plt.axis('off')
        
        plt.subplot(2, 2, 2)
        plt.title("Tongue Segmentation")
        plt.imshow(segmentation_viz)
        plt.axis('off')
        
        plt.subplot(2, 2, 3)
        plt.title("Detected Papillae")
        plt.imshow(visualization)
        plt.axis('off')
        
        plt.subplot(2, 2, 4)
        plt.title("Papillae Size vs Redness")
        if len(results_df) > 0:
            plt.scatter(
                results_df['size'], 
                results_df['redness_score'], 
                c=results_df['redness_score'], 
                cmap='coolwarm',
                alpha=0.7
            )
            plt.colorbar(label='Redness Score')
            plt.xlabel('Papilla Size (pixels)')
            plt.ylabel('Redness Score')
        else:
            plt.text(0.5, 0.5, "No papillae detected", ha='center', va='center')
        
        plt.tight_layout()
        plt.savefig(viz_path)
        plt.close()
        
        if len(results_df) > 0:
            csv_path = os.path.join(OUTPUT_DIR, f"papillae_{uuid.uuid4()}.csv")
            results_df.to_csv(csv_path, index=False)
        
        logger.info("Papillae analysis completed")
        
        return {
            "total_papillae": report['total_papillae'],
            "avg_size": float(report['avg_size']),
            "avg_redness": float(report['avg_redness']),
        }
    except Exception as e:
        logger.error(f"Error in papillae analysis: {str(e)}")
        return {
            "total_papillae": 0,
            "avg_size": 0.0,
            "avg_redness": 0.0,
        }

def detect_cracks(image_path: str) -> Dict[str, Any]:
    """Detect tongue cracks"""
    if not CRACK_DETECTION_AVAILABLE:
        logger.warning("Crack detection not available, returning default values")
        morphed = os.path.join(OUTPUT_DIR, f"crack_{uuid.uuid4()}.jpg")
        image = cv2.imread(image_path)
        if image is not None:
            cv2.imwrite(morphed, image)
        return {"morph": morphed, "score": 0.0}
    
    try:
        from Tongue_crack_detection_model import detect_tongue_cracks_advanced
        
        result = detect_tongue_cracks_advanced(image_path)
        if result is None:
            raise Exception("Crack detection returned None")
        
        morphed = os.path.join(OUTPUT_DIR, f"crack_{uuid.uuid4()}.jpg")
        if "overlay" in result and result["overlay"] is not None:
            cv2.imwrite(morphed, result["overlay"])
        
        score = result.get("score", 0.0)
        logger.info(f"Crack detection completed with score: {score}")
        return {"morph": morphed, "score": score}
    except Exception as e:
        logger.error(f"Error in crack detection: {str(e)}")
        morphed = os.path.join(OUTPUT_DIR, f"crack_{uuid.uuid4()}.jpg")
        image = cv2.imread(image_path)
        if image is not None:
            cv2.imwrite(morphed, image)
        return {"morph": morphed, "score": 0.0}

def get_jagged_score(image_path: str) -> Dict[str, Any]:
    """Get jagged tongue score"""
    if not JAGGED_SCORE_AVAILABLE:
        logger.warning("Jagged score calculation not available")
        return {"score": 0.0}
    
    try:
        from jaggedScore import jagged_tongue
        
        result = jagged_tongue(image_path)
        logger.info(f"Jagged score calculated: {result['score']}")
        return result
    except Exception as e:
        logger.error(f"Error in jagged score calculation: {str(e)}")
        return {"score": 0.0}

def generate_ai_summary(response_data: Dict[str, Any]) -> str:
    """Generate AI summary using LLM"""
    if not LLM_AVAILABLE:
        logger.warning("LLM not available, returning default summary")
        return "Tongue analysis completed. Please consult a healthcare professional for interpretation."
    
    try:
        from llmcall import generate_summary
        
        summary_response = generate_summary(response_data)
        return summary_response.get("reply", "Analysis completed")
    except Exception as e:
        logger.error(f"Error generating summary: {str(e)}")
        return "Analysis completed. Please consult a healthcare professional for interpretation."
API_KEY = "AIzaSyBWb5O_8-tYNazvqOAjBWdcqmU--JF-EAg"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.post("/chat")
async def chat(request: Request):
    """Handle chat messages"""
    try:
        data = await request.json()
        user_message = data.get("message", "").strip()
        if not user_message:
            raise HTTPException(status_code=400, detail="Please enter a message.")

        logger.info(f"Received message: {user_message[:30]}...")

        if not LLM_AVAILABLE:
            return {"reply": "LLM service not available. Please ensure llmcall module is properly configured."}

        payload = {
            "contents": [{
                "parts": [{"text": user_message}]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 1024,
            }
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        response_data = response.json()

        try:
            reply = response_data["candidates"][0]["content"]["parts"][0]["text"]
            logger.info(f"Generated response: {reply[:30]}...")
            return {"reply": reply}
        except (KeyError, IndexError) as e:
            logger.error(f"Error parsing API response: {e}")
            return {"reply": "Error parsing response from API."}

    except requests.exceptions.RequestException as e:
        logger.error(f"API request error: {e}")
        raise HTTPException(status_code=502, detail=f"API Error: {str(e)}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
@app.post("/analyze_tongue", response_class=JSONResponse)
async def analyze_tongue(file: UploadFile = File(...)):
    """Analyze a tongue image for segmentation, white coating, and papillae detection"""
    start_time = time.time()
    logger.info(f"Received request to analyze tongue image: {file.filename}")
    
    try:
        file_path = save_uploaded_file(file)
        logger.info(f"Saved file to {file_path}")
        
        image = cv2.imread(file_path)
        if image is None:
            raise HTTPException(status_code=400, detail="Could not read image file")
        
        # Step 1: Detect tongue point
        input_point = detect_tongue_roboflow(image)
        
        # Step 2: Segment tongue
        segmented_image, mask = segment_tongue_sam(image, input_point)
        
        # Save segmented image
        segmented_path = os.path.join(OUTPUT_DIR, f"segmented_{uuid.uuid4()}.jpg")
        cv2.imwrite(segmented_path, segmented_image)
        
        # Step 3: Detect white coating
        coating_results = detect_white_coating(segmented_image, mask)
        
        # Step 4: Analyze papillae
        papillae_results = analyze_papillae(segmented_path)
        redness = papillae_results["avg_redness"] * 10
        
        # Step 5: Detect cracks
        crack_results = detect_cracks(segmented_path)
        
        # Step 6: Calculate jagged score
        jagged_result = get_jagged_score(segmented_path)
        
        # Step 7: Calculate health scores
        Nutrition_Score = round(
            ((10 - coating_results["white_coating_percentage"]/7) * 0.4 + 
             papillae_results["avg_size"] * 0.3 + 
             papillae_results["avg_redness"] * 0.3) * 10, 2
        )
        
        Mantle_Score = round(
            ((10 - crack_results["score"]/10) * 0.5 + (10 - 5) * 0.5) * 10, 2
        )
        
        # Prepare initial response
        initial_response = {
            "Jaggedness": jagged_result["score"] * 10,
            "Cracks": crack_results,
            "redness": redness,
            "segmented_image_path": segmented_path,
            "white_coating": coating_results,
            "papillae_analysis": papillae_results,
            "NutritionScore": Nutrition_Score,
            "MantleScore": Mantle_Score,
        }
        
        # Step 8: Generate AI summary
        summary = generate_ai_summary(initial_response)
        
        # Final response
        response = {
            "Jaggedness": initial_response["Jaggedness"],
            "Summary": summary,
            "Cracks": crack_results,
            "NutritionScore": Nutrition_Score,
            "MantleScore": Mantle_Score,
            "redness": redness,
            "segmented_image_path": segmented_path,
            "white_coating": coating_results,
            "papillae_analysis": papillae_results
        }
        
        elapsed = time.time() - start_time
        logger.info(f"Analysis completed in {elapsed:.2f} seconds")
        
        return JSONResponse(content=response)
    
    except HTTPException as http_exc:
        logger.error(f"HTTP exception: {http_exc.detail}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/image/{image_path:path}")
async def get_image(image_path: str):
    """Retrieve an image from the output directory"""
    full_path = os.path.join(OUTPUT_DIR, os.path.basename(image_path))
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(full_path)

@app.get("/csv/{csv_path:path}")
async def get_csv(csv_path: str):
    """Retrieve a CSV file from the output directory"""
    full_path = os.path.join(OUTPUT_DIR, os.path.basename(csv_path))
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="CSV file not found")
    return FileResponse(full_path)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    health_status = {
        "status": "healthy",
        "sam_model": "loaded" if SAM_AVAILABLE else "not loaded",
        "roboflow_client": "loaded" if ROBOFLOW_AVAILABLE else "not loaded",
        "papillae_analyzer": "available" if PAPILLAE_AVAILABLE else "unavailable",
        "crack_detection": "available" if CRACK_DETECTION_AVAILABLE else "unavailable",
        "jagged_score": "available" if JAGGED_SCORE_AVAILABLE else "unavailable",
        "llm_service": "available" if LLM_AVAILABLE else "unavailable",
    }
    return JSONResponse(content=health_status)

if __name__ == "__main__":
    uvicorn.run("FastApiServer:app", host="0.0.0.0", port=8000, reload=True)