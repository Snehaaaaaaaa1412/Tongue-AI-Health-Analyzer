# Tongue AI Analysis Frontend

Complete React frontend for the Tongue Analysis API.

## Setup Instructions

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm start
```

The app will open at `http://localhost:3000`

### 3. Build for Production
```bash
npm run build
```

## Features

- ✅ Drag & Drop Image Upload
- ✅ Image Preview
- ✅ Real-time Analysis
- ✅ Beautiful Results Display
- ✅ Toast Notifications
- ✅ Responsive Design
- ✅ Mobile Friendly
- ✅ Error Handling
- ✅ Loading States

## API Configuration

Backend URL: `http://127.0.0.1:8000`

Edit `src/services/api.js` to change the API endpoint.

## File Structure

```
frontend/
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
│   └── index.js
├── tailwind.config.js
├── postcss.config.js
├── package.json
└── .gitignore
```

## Troubleshooting

### CORS Issues
Make sure backend is running with CORS enabled:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Port Conflicts
If port 3000 is in use, run:
```bash
PORT=3001 npm start
```

### API Connection Failed
1. Ensure backend is running on `http://127.0.0.1:8000`
2. Check browser console for errors
3. Verify CORS configuration

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
