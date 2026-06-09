# 🧠 Tongue Analysis AI System

Complete end-to-end system for advanced tongue health analysis using FastAPI backend and React frontend.

## 🚀 Quick Start (All Platforms)

### Windows (Easiest)
```batch
# Run the batch file
start.bat
```

Or PowerShell:
```powershell
.\start.ps1
```

### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install backend dependencies
pip install -r requirements.txt

# In another terminal, start frontend
cd frontend
npm install
npm start

# Run backend
python -m uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📋 Manual Setup

### Backend Setup
```bash
# 1. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run server
uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload
```

**Backend runs on:** `http://localhost:8000`

### Frontend Setup
```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm start
```

**Frontend runs on:** `http://localhost:3000`

---

## 🏗️ Project Structure

```
HealthLingue/
├── FastApiServer.py                 # Main backend
├── requirements.txt                 # Python dependencies
├── tongue_*.py                      # Analysis modules
├── jaggedScore.py
├── llmcall.py
├── segment.py
├── evaluate.py
├── chat.py
├── SETUP_GUIDE.md                  # Detailed setup guide
├── start.bat                        # Windows quick start
├── start.ps1                        # PowerShell quick start
│
└── frontend/                        # React application
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── components/
    │   │   ├── ImageUpload.jsx
    │   │   └── ResultsDisplay.jsx
    │   ├── services/
    │   │   └── api.js
    │   ├── App.jsx
    │   ├── App.css
    │   ├── index.js
    │   └── index.css
    ├── package.json
    ├── tailwind.config.js
    └── postcss.config.js
```

---

## 🎯 Features

### Backend (FastAPI)
✅ Image upload & processing  
✅ Tongue segmentation (SAM)  
✅ White coating detection  
✅ Papillae analysis  
✅ Crack detection  
✅ Jaggedness scoring  
✅ AI-generated health summary  
✅ CORS enabled  
✅ Graceful fallbacks for missing dependencies  

### Frontend (React)
✅ Modern UI with Tailwind CSS  
✅ Drag & drop file upload  
✅ Image preview  
✅ Real-time analysis  
✅ Beautiful results display  
✅ Toast notifications  
✅ Responsive design  
✅ Error handling  
✅ Loading states  

---

## 🔌 API Endpoints

### Health Check
```
GET http://127.0.0.1:8000/health
```

### Analyze Tongue
```
POST http://127.0.0.1:8000/analyze_tongue
Headers: Content-Type: multipart/form-data
Body: file (image)

Response:
{
  "Jaggedness": 25.0,
  "Summary": "AI-generated summary...",
  "Cracks": {"morph": "path", "score": 3.5},
  "NutritionScore": 75.5,
  "MantleScore": 82.5,
  "redness": 6.8,
  "segmented_image_path": "path",
  "white_coating": {"white_coating_percentage": 15.3, ...},
  "papillae_analysis": {"total_papillae": 127, ...}
}
```

### Chat
```
POST http://127.0.0.1:8000/chat
Body: {"message": "Your question here"}
```

### Get Image
```
GET http://127.0.0.1:8000/image/{image_path}
```

### Get CSV
```
GET http://127.0.0.1:8000/csv/{csv_path}
```

---

## 🛠️ Tech Stack

### Backend
- **Framework:** FastAPI
- **Server:** Uvicorn
- **ML/CV:** OpenCV, PyTorch, Segment Anything
- **APIs:** Roboflow, Gemini
- **Data:** NumPy, Pandas, Matplotlib

### Frontend
- **Framework:** React 18
- **Styling:** Tailwind CSS
- **HTTP:** Axios
- **Notifications:** React Hot Toast
- **Build:** Create React App

---

## 🔧 Configuration

### Backend
Edit `FastApiServer.py` for:
- Port (default: 8000)
- Host (default: 0.0.0.0)
- CORS settings
- API keys (Roboflow, Gemini)

### Frontend
Edit `frontend/src/services/api.js` for:
- API base URL
- Timeout settings
- Headers

Or create `.env`:
```
REACT_APP_API_BASE_URL=http://127.0.0.1:8000
```

---

## ⚠️ Important Notes

### Optional Dependencies
These dependencies are optional and have graceful fallbacks:
- `segment_anything` - Uses simple HSV thresholding if not available
- `inference_sdk` (Roboflow) - Uses image center if unavailable
- `llmcall` (Gemini API) - Uses generic response if unavailable

### SAM Model
Download and place in project root:
```
https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
```
Rename to: `sam_vit_h.pth`

### API Keys
Required for full functionality:
- **Roboflow API Key:** (in FastApiServer.py)
- **Gemini API Key:** (in FastApiServer.py & llmcall.py)

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Clear pip cache
pip cache purge

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

### Frontend Won't Start
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
npm start
```

### CORS Errors
Backend CORS is enabled by default. If issues persist:
```python
# Verify in FastApiServer.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### API Connection Failed
1. ✅ Backend running? `http://127.0.0.1:8000/health`
2. ✅ Frontend on correct port? `http://localhost:3000`
3. ✅ Check browser console (F12 → Console tab)
4. ✅ Check Network tab for failed requests

### Port Already in Use
```bash
# Change backend port
uvicorn FastApiServer:app --port 8001

# Change frontend port
PORT=3001 npm start
```

---

## 📊 Performance

### Optimization Tips
- Use GPU for faster processing (set `DEVICE = "cuda"`)
- Compress images before upload (< 5MB recommended)
- Use production build for frontend deployment

### Build Production
```bash
# Backend
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker FastApiServer:app

# Frontend
cd frontend
npm run build
# Output in: frontend/build/
```

---

## 📚 Documentation

- [Backend Details](SETUP_GUIDE.md)
- [Frontend Details](frontend/FRONTEND_README.md)
- [API Documentation](https://127.0.0.1:8000/docs) (when backend running)

---

## ⚖️ Disclaimer

This system is for **educational and informational purposes only**. It is NOT a substitute for professional medical diagnosis or treatment. Always consult a qualified healthcare professional for medical advice.

---

## 📝 License

MIT License - See LICENSE file

---

## 🎉 Ready to Go!

Your system is now complete and ready to use. Visit:
- **Backend:** http://localhost:8000
- **Frontend:** http://localhost:3000

**Enjoy advanced tongue health analysis! 🧠💪**
