<div align="center">

# 🧬 Tongue AI Health Analyzer

**AI-powered tongue image analysis for oral health diagnostics**

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=flat&logo=opencv&logoColor=white)

</div>

---

## 📌 Overview

Upload a tongue photo → get an instant AI-powered health report.

The system uses **Computer Vision** to detect tongue abnormalities and **Google Gemini** to generate a plain-English health summary — no medical knowledge required.

> ⚠️ For educational and health awareness purposes only. Not a substitute for professional medical advice.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 Tongue Segmentation | Isolates tongue from any background using Meta SAM |
| 🤍 White Coating Detection | Measures coating coverage percentage |
| 🔍 Crack Detection | Scores surface fissures from 0–10 |
| 🔴 Redness Analysis | Measures average inflammation level |
| 🔬 Papillae Analysis | Counts taste buds, measures size & redness |
| 📐 Jaggedness Analysis | Detects irregular tongue edges |
| 🍎 Nutrition Score | Estimates nutritional health from tongue indicators |
| 🛡️ Mantle Score | Overall tongue surface health score |
| 🤖 AI Health Summary | Gemini-powered natural language health report |

---

## 🛠️ Tech Stack

**Frontend**
- React.js — Interactive dashboard UI
- Axios — API communication
- CSS3 — Dark-theme custom styling

**Backend**
- FastAPI — High-performance async Python API
- Uvicorn — ASGI production server

**AI / Computer Vision**
- OpenCV — Edge detection, color analysis, morphological ops
- PyTorch — Deep learning runtime
- Segment Anything Model (SAM) — Tongue segmentation
- PIL / NumPy / Matplotlib — Image processing & visualization
- Pandas — Data export to CSV

**External Services**
- Google Gemini API — AI health summary generation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           React.js Frontend             │
│   Upload → Preview → Results Dashboard  │
└──────────────────┬──────────────────────┘
                   │  POST /analyze
                   ▼
┌─────────────────────────────────────────┐
│           FastAPI Backend               │
│                                         │
│  Image → SAM Segmentation               │
│       → White Coating (HSV)             │
│       → Crack Detection (Canny)         │
│       → Papillae Detection (Blob)       │
│       → Redness / Jaggedness Analysis   │
│       → Score Calculation               │
│       → Gemini API (AI Summary)         │
│       → CSV Export                      │
└──────────────────┬──────────────────────┘
                   │
         ┌─────────▼──────────┐
         │   Google Gemini    │
         │   (LLM Summary)    │
         └────────────────────┘
```

---

## 🤖 AI Models Explained

**Segment Anything Model (SAM)**
Meta's foundation model for image segmentation. Isolates the tongue from any background — photos on white, green, or complex backgrounds all work reliably. Traditional thresholding methods fail here; SAM understands semantic boundaries.

**Crack Detection (OpenCV Canny)**
Converts tongue to grayscale → Gaussian blur → Canny edge detection → morphological closing. Crack pixels normalized to a 0–10 score.

**White Coating Detection**
Converts image to HSV color space → masks whitish-gray pixel range → calculates coverage percentage. HSV is more robust to lighting changes than RGB.

**Papillae Detection**
CLAHE contrast enhancement → blob detection → contour analysis. Counts individual papillae, measures average size and redness per structure.

---

## ⚡ Why These Technologies?

| Choice | Reason |
|--------|--------|
| **FastAPI** | Native async support handles slow ML inference without blocking. Auto-generates Swagger docs. 3× faster than Flask for concurrent requests. |
| **React.js** | Component-based architecture perfectly matches the multi-card dashboard (coating, cracks, papillae each update independently). |
| **SAM Model** | Outperforms thresholding/GrabCut on real-world photos with varied skin tones and backgrounds. Zero fine-tuning needed. |
| **Gemini API** | Converts raw CV numbers into readable health language. Supports 40+ languages for global reach. |

**Fallback Logic**
If Gemini API fails (timeout / rate limit), the system returns all CV metrics normally. The `ai_summary` field returns a templated message and the API responds with HTTP `206 Partial Content` — users always get their analysis results.

---

## 📸 Screenshots

### 🏠 Homepage
![Homepage](screenshots/homepage.png)

### 📤 Upload Screen
![Upload](screenshots/upload.png)

### 📊 Analysis Dashboard
![Dashboard](screenshots/dashboard.png)

### 🔧 Swagger API Docs
![Swagger](screenshots/swagger.png)

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- Google Gemini API key

### Backend
```bash
git clone https://github.com/Snehaaaaaaaa1412/Tongue-AI-Health-Analyzer.git
cd Tongue-AI-Health-Analyzer/backend

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Download SAM weights (~2.5 GB)
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth -O models/sam_vit_h.pth

# Add your API key
echo "GEMINI_API_KEY=your_key_here" > .env
```

### Frontend
```bash
cd ../frontend
npm install
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

---

## ▶️ Run

```bash
# Terminal 1 — Backend
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2 — Frontend
cd frontend && npm start
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

---

## 📊 Sample Results

| Condition | Coating % | Crack Score | Papillae | Redness | Status |
|-----------|-----------|-------------|----------|---------|--------|
| Healthy | <15% | <2.0 | 600–900 | <0.5 | 🟢 Healthy |
| White Coated | >40% | <3.0 | 400–600 | 0.4–0.6 | 🟠 Moderate |
| Cracked | <20% | >5.0 | 300–500 | >0.7 | 🟠 Moderate |
| Inflamed | <20% | <3.0 | 400–700 | >0.8 | 🔴 Concern |

---

## 🔮 Future Improvements

- [ ] Mobile camera capture via WebRTC
- [ ] Longitudinal health trend tracking
- [ ] Lightweight custom CNN to replace SAM (10× faster)
- [ ] PDF health report download
- [ ] Telemedicine integration via HL7 FHIR API
- [ ] Multi-language AI summaries

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
Built with ❤️ for accessible healthcare · Give it a ⭐ if you find it useful!
</div>
