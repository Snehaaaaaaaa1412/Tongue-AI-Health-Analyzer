# Tongue Analysis AI System - Complete Setup Guide

## Project Structure

```
HealthLingue-main/
├── FastApiServer.py          # FastAPI backend
├── requirements.txt          # Python dependencies
├── [other backend files]
└── frontend/                 # React frontend
    ├── src/
    ├── public/
    ├── package.json
    └── [other frontend files]
```

## Backend Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows CMD:**
```bash
venv\Scripts\activate
```

**Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download SAM Model (Optional)
```bash
# Download from: https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
# Save as: sam_vit_h.pth in project root
```

### 5. Run Backend Server
```bash
uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload
```

Backend will be available at: `http://localhost:8000`

Check health: `http://localhost:8000/health`

## Frontend Setup

### 1. Navigate to Frontend Directory
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start Development Server
```bash
npm start
```

Frontend will open at: `http://localhost:3000`

## Testing the System

1. **Backend Running?** Visit `http://localhost:8000/health`
2. **Frontend Running?** Visit `http://localhost:3000`
3. **Try Upload:** Select a tongue image and click "Analyze Image"
4. **Check Results:** View analysis scores and summary

## API Endpoints

### Health Check
```
GET http://127.0.0.1:8000/health
```

### Analyze Tongue
```
POST http://127.0.0.1:8000/analyze_tongue
Content-Type: multipart/form-data
Body: file (image)
```

### Retrieve Image
```
GET http://127.0.0.1:8000/image/{image_path}
```

### Retrieve CSV
```
GET http://127.0.0.1:8000/csv/{csv_path}
```

## Troubleshooting

### Backend Issues

**Import Error:**
- Ensure all packages are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (requires 3.8+)

**Port Already in Use:**
```bash
uvicorn FastApiServer:app --host 0.0.0.0 --port 8001 --reload
```

**SAM Model Not Found:**
- Download and place `sam_vit_h.pth` in project root
- Or create empty file: `touch sam_vit_h.pth`
- System will gracefully handle missing optional models

### Frontend Issues

**CORS Errors:**
- Backend CORS is enabled by default
- If issues persist, update `src/services/api.js`

**Port 3000 in Use:**
```bash
PORT=3001 npm start
```

**Dependencies Not Installing:**
```bash
npm cache clean --force
npm install
```

## Production Build

### Frontend
```bash
cd frontend
npm run build
```

Output will be in `frontend/build/`

### Backend
Use a production ASGI server:
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker FastApiServer:app
```

## Environment Variables

Create `.env` in frontend directory:
```
REACT_APP_API_BASE_URL=http://127.0.0.1:8000
```

## Support

For issues or questions:
1. Check server logs (terminal where server is running)
2. Check browser console (F12 in browser)
3. Verify both backend and frontend are running
4. Ensure firewall allows ports 8000 and 3000

---

**System is ready to use!** 🚀
