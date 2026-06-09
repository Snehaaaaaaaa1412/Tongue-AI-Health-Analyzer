# 🧠 Tongue Analysis AI System - React Frontend

Complete, production-ready React frontend for advanced tongue health analysis.

## ⚡ Quick Start

### Prerequisites
- Node.js 14+ and npm
- Backend running on `http://127.0.0.1:8000`

### Install & Run
```bash
cd frontend
npm install
npm start
```

Open `http://localhost:3000` in your browser.

---

## 📁 Project Structure

```
frontend/
├── public/
│   └── index.html                 # Main HTML
├── src/
│   ├── components/
│   │   ├── ImageUpload.jsx        # Drag & drop upload
│   │   └── ResultsDisplay.jsx     # Results visualization
│   ├── services/
│   │   └── api.js                 # API client
│   ├── App.jsx                    # Main app
│   ├── App.css                    # Styling
│   ├── index.js                   # Entry point
│   └── index.css                  # Global styles
├── tailwind.config.js             # Tailwind config
├── postcss.config.js              # PostCSS config
├── package.json                   # Dependencies
└── README.md                       # This file
```

---

## 🎨 Features

### Image Upload
- Drag & drop support
- Click to select
- Image preview
- File validation

### Analysis Results
- Nutrition Score
- Mantle Health
- Jaggedness Score
- Redness Analysis
- White Coating Detection
- Papillae Analysis
- Crack Detection
- AI Summary

### UI/UX
- Responsive design (mobile & desktop)
- Loading spinner
- Toast notifications
- Error handling
- Health status indicator

---

## 🔧 Configuration

### API Base URL

Edit `src/services/api.js`:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000';
```

Or use environment variable in `.env`:
```
REACT_APP_API_BASE_URL=http://your-backend-url
```

Then update `api.js`:
```javascript
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000';
```

---

## 📦 Dependencies

```json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "axios": "^1.6.0",
  "react-hot-toast": "^2.4.1",
  "tailwindcss": "^3.3.0"
}
```

---

## 🚀 Development

### Available Scripts

```bash
# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Eject (one-way operation)
npm eject
```

---

## 🐛 Troubleshooting

### CORS Errors
**Solution:** Backend must have CORS enabled:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Port 3000 Already in Use
```bash
PORT=3001 npm start
```

### API Connection Failed
1. ✅ Backend running on `http://127.0.0.1:8000`?
2. ✅ Check browser console (F12)
3. ✅ Check network tab for 500 errors
4. ✅ Verify CORS configuration

### Blank Page
1. ✅ Clear browser cache
2. ✅ Restart dev server: `npm start`
3. ✅ Check console for errors (F12)

### Dependencies Issue
```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

---

## 📱 Responsive Design

Tested on:
- Desktop (1920x1080, 1440x900, 1024x768)
- Tablet (768x1024, 810x1080)
- Mobile (375x667, 414x896)

---

## ♿ Accessibility

- Semantic HTML
- ARIA labels on interactive elements
- Keyboard navigation support
- Color contrast compliance
- Touch-friendly buttons (min 48px)

---

## 🔐 Security

- Input validation
- File type checking
- XSS protection via React escaping
- CSRF token support (if backend requires)

---

## 📊 Performance

- Lazy loading images
- Efficient re-renders with React hooks
- Minified production build
- Gzip compression ready

---

## 🌐 Browser Support

| Browser | Support |
|---------|---------|
| Chrome  | ✅ 90+  |
| Firefox | ✅ 88+  |
| Safari  | ✅ 14+  |
| Edge    | ✅ 90+  |

---

## 🎓 Learning Resources

- [React Docs](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [Axios](https://axios-http.com)
- [React Hot Toast](https://react-hot-toast.com)

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🤝 Support

For issues:
1. Check console errors (F12)
2. Verify backend is running
3. Check network requests in DevTools
4. Review SETUP_GUIDE.md

---

**Made with ❤️ for healthcare AI** 🏥
