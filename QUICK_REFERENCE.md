# Quick Reference

## 🚀 Commands

### Backend
```bash
# Activate environment
venv\Scripts\activate                    # Windows
source venv/bin/activate                 # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload

# Run with different port
uvicorn FastApiServer:app --port 8001

# Install new package
pip install package_name
pip freeze > requirements.txt
```

### Frontend
```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development
npm start

# Build for production
npm run build

# Install new package
npm install package_name

# Update all packages
npm update
```

---

## 🔗 URLs

| Component | URL |
|-----------|-----|
| Frontend App | http://localhost:3000 |
| Backend API | http://127.0.0.1:8000 |
| Swagger Docs | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |
| Health Check | http://127.0.0.1:8000/health |

---

## 📡 API Quick Reference

### Test Health
```bash
curl http://127.0.0.1:8000/health
```

### Test Image Upload (PowerShell)
```powershell
$form = @{
    file = Get-Item "C:\path\to\image.jpg"
}
Invoke-WebRequest -Uri "http://127.0.0.1:8000/analyze_tongue" `
    -Method Post -Form $form
```

### Test Image Upload (Bash)
```bash
curl -X POST -F "file=@/path/to/image.jpg" \
  http://127.0.0.1:8000/analyze_tongue
```

---

## 🔧 Configuration Files

| File | Purpose | Location |
|------|---------|----------|
| `requirements.txt` | Python dependencies | Root |
| `package.json` | Node dependencies | frontend/ |
| `.env` | Environment variables | frontend/ |
| `tailwind.config.js` | Tailwind config | frontend/ |
| `FastApiServer.py` | Backend config | Root |

---

## 📂 Important Directories

```
frontend/
  src/
    components/      # React components
    services/        # API client
  public/           # Static files
  node_modules/     # Dependencies

HealthLingue/
  output/           # Analysis output
  image_results/    # Test results
```

---

## 🔑 Key Files to Edit

### For Backend Changes
1. `FastApiServer.py` - Main app
2. `requirements.txt` - Dependencies
3. `llmcall.py` - LLM integration
4. `Tongue_crack_detection_model.py` - Crack detection

### For Frontend Changes
1. `frontend/src/App.jsx` - Main component
2. `frontend/src/services/api.js` - API calls
3. `frontend/tailwind.config.js` - Styling
4. `frontend/package.json` - Dependencies

---

## 🐛 Debug Tips

### Backend Debug
```python
# Add to FastApiServer.py
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Use in functions
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

### Frontend Debug
```javascript
// Check API connection
console.log('Sending to:', API_BASE_URL);

// Log response
console.log('Response:', response);

// Use debugger
debugger; // Pauses execution
```

### Check Logs
```bash
# Backend logs appear in terminal running uvicorn
# Frontend logs appear in browser console (F12)
# Network logs in DevTools → Network tab
```

---

## 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| Port 8000 in use | `uvicorn FastApiServer:app --port 8001` |
| Port 3000 in use | `PORT=3001 npm start` |
| CORS error | Check backend CORSMiddleware |
| 404 Not Found | Check endpoint URL spelling |
| Module not found | `pip install -r requirements.txt` |
| npm ERR! | `npm cache clean --force && npm install` |
| Image upload fails | Check file size and type |
| API timeout | Backend taking too long, check logs |

---

## 📊 Testing Quick Commands

```bash
# Test backend health
curl http://127.0.0.1:8000/health

# Test backend is running
ping 127.0.0.1:8000

# Check ports in use (Windows)
netstat -ano | findstr :8000

# Check ports in use (macOS/Linux)
lsof -i :8000

# Kill process on port 8000 (macOS/Linux)
kill -9 $(lsof -t -i :8000)
```

---

## 📚 Documentation Links

- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Docs](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [Axios](https://axios-http.com)
- [Python Docs](https://python.org/docs)

---

## 🎯 Performance Tuning

### Backend
```python
# Enable GPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Increase workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker FastApiServer:app
```

### Frontend
```bash
# Build analysis
npm run build -- --analyze

# Optimize images
npm install --save-dev image-minimizer-webpack-plugin
```

---

## 🔐 Security Checklist

- [ ] API keys not in source code
- [ ] CORS properly configured
- [ ] Input validation enabled
- [ ] Error messages don't leak info
- [ ] HTTPS enabled in production
- [ ] Rate limiting configured

---

## 📋 Deployment Checklist

### Backend
- [ ] Requirements.txt up to date
- [ ] Environment variables configured
- [ ] Logging configured
- [ ] Error handling complete
- [ ] SAM model available

### Frontend
- [ ] Production build created
- [ ] Environment variables set
- [ ] API URL configured
- [ ] Dependencies updated
- [ ] Console errors fixed

---

**Print this page for quick reference! 📖**
