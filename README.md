# 👅 Tongue AI Health Analyzer

An AI-powered healthcare web application that analyzes tongue images using Computer Vision, Deep Learning, and FastAPI to provide preliminary tongue health insights and automated health scoring.

The system combines advanced image processing, machine learning models, and AI-generated summaries to evaluate multiple tongue health indicators such as white coating, cracks, papillae density, redness, and edge irregularities.

---

# 🚀 Features

## 🔍 AI-Based Tongue Analysis

* Tongue segmentation using Segment Anything Model (SAM)
* White coating detection and percentage calculation
* Tongue crack detection and scoring
* Papillae detection and analysis
* Jagged edge detection
* Redness analysis

---

## 📊 Health Scoring Engine

The application generates multiple health-related scores:

* Nutrition Score
* Mantle Health Score
* Redness Index
* Edge Irregularity Score

---

## 🤖 AI Health Summary

* Gemini API based AI-generated health report
* Rule-based fallback summary system
* Human-readable tongue analysis insights

---

## 🌐 Full Stack Web Application

* React.js Frontend
* FastAPI Backend
* REST API Architecture
* Interactive Dashboard UI

---

# 🧠 System Architecture

```text
                 ┌────────────────────────────┐
                 │        USER (Browser)      │
                 │  React Frontend UI        │
                 │  - Image Upload           │
                 │  - Results Dashboard      │
                 └────────────┬──────────────┘
                              │ HTTP (Axios / Fetch)
                              ▼
        ┌────────────────────────────────────────┐
        │           FASTAPI BACKEND             │
        │  (Python REST API Server)            │
        │                                      │
        │  Endpoints:                          │
        │  - /health                           │
        │  - /analyze_tongue                   │
        │  - /chat                             │
        └────────────┬─────────────────────────┘
                     │
                     ▼
   ┌────────────────────────────────────────────┐
   │           AI PROCESSING LAYER              │
   │                                            │
   │  🧠 Image Preprocessing (OpenCV, PIL)      │
   │  🧠 Feature Extraction                      │
   │                                            │
   │  ├── Tongue Crack Detection Model          │
   │  ├── Papillae Analysis Module              │
   │  ├── Jaggedness Score Calculator           │
   │  ├── White Coating Detection               │
   │                                            │
   │  🧩 Segment Anything Model (SAM)           │
   │      (Optional Segmentation Layer)         │
   └────────────┬───────────────────────────────┘
                │
                ▼
   ┌────────────────────────────────────────────┐
   │         HEALTH SCORING ENGINE              │
   │                                            │
   │  - Nutrition Score                         │
   │  - Mantle Score                            │
   │  - Redness Index                           │
   │  - Edge Irregularity Score                 │
   └────────────┬───────────────────────────────┘
                │
                ▼
   ┌────────────────────────────────────────────┐
   │         AI SUMMARY LAYER                   │
   │                                            │
   │  🤖 Gemini API (LLM)                       │
   │  - Generates Health Report                 │
   │  - Text-based Medical Summary              │
   │                                            │
   │  ⚠️ Fallback: Rule-based Summary           │
   └────────────┬───────────────────────────────┘
                │
                ▼
        ┌────────────────────────────┐
        │      JSON RESPONSE         │
        │                            │
        │ scores + analysis + text   │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │     React Frontend UI      │
        │                            │
        │  📊 Score Cards            │
        │  📈 Health Dashboard       │
        │  🧾 AI Summary Panel       │
        └────────────────────────────┘
```

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Axios
* CSS

## Backend

* FastAPI
* Python
* Uvicorn

## AI / Machine Learning

* OpenCV
* PyTorch
* NumPy
* Pandas
* Matplotlib
* Segment Anything Model (SAM)

---

# 📂 Project Structure

```text
Tongue-AI-Health-Analyzer/
│
├── frontend/                         # React Frontend
│
├── FastApiServer.py                  # Main FastAPI Backend
├── segment.py                        # Tongue Segmentation
├── Tongue_crack_detection_model.py   # Crack Detection
├── tongue_papillae_analyzer.py       # Papillae Analysis
├── jaggedScore.py                    # Jaggedness Calculation
├── llmcall.py                        # Gemini API Integration
│
├── output/                           # Generated Results
├── sam_vit_h.pth                     # SAM Model Checkpoint
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Snehaaaaaaaa1412/Tongue-AI-Health-Analyzer.git
cd Tongue-AI-Health-Analyzer
```

---

# 🐍 Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend Server

```bash
uvicorn FastApiServer:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

# 📡 API Endpoints

## 🔍 Analyze Tongue

```http
POST /analyze_tongue
```

Uploads a tongue image and returns detailed AI analysis.

---

## 💬 Chat Endpoint

```http
POST /chat
```

AI-based health discussion endpoint.

---

## 🩺 Health Check

```http
GET /health
```

Returns server and model status.

---

# 📊 Sample Output

```json
{
  "NutritionScore": 98.64,
  "MantleScore": 74.13,
  "Jaggedness": 65.98,
  "redness": 7.92,
  "white_coating_percentage": 25.11
}
```

---

# 🧪 AI Models & Modules

| Model / Module        | Purpose               |
| --------------------- | --------------------- |
| SAM Model             | Tongue Segmentation   |
| Crack Detection Model | Crack Analysis        |
| Papillae Analyzer     | Papillae Detection    |
| Jaggedness Algorithm  | Edge Analysis         |
| Gemini API            | AI Summary Generation |

---

# ⚠️ Disclaimer

This project is developed for educational and research purposes only.

It should not be considered a replacement for professional medical diagnosis or healthcare consultation.

Always consult certified medical professionals for accurate diagnosis and treatment.

---

# 🚀 Future Improvements

* Real-time tongue analysis
* Advanced medical dataset training
* Mobile application support
* Cloud deployment
* AI chatbot enhancement
* Multi-language support
* Enhanced health prediction models

---

# 👩‍💻 Developer

Sneha
B.Tech CSE Student
AI + Full Stack Developer

GitHub:
https://github.com/Snehaaaaaaaa1412

---

# ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
