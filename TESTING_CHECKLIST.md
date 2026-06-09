# Testing Checklist

## Backend Testing

### Startup
- [ ] Backend starts without errors
- [ ] Listens on `http://127.0.0.1:8000`
- [ ] Health endpoint accessible: `GET /health`
- [ ] Swagger docs available: `http://127.0.0.1:8000/docs`

### Endpoints
- [ ] GET `/` returns welcome message
- [ ] GET `/health` returns system status
- [ ] POST `/analyze_tongue` accepts image
- [ ] POST `/analyze_tongue` returns valid JSON
- [ ] GET `/image/{path}` serves images
- [ ] GET `/csv/{path}` serves CSV files
- [ ] POST `/chat` accepts message

### Error Handling
- [ ] Invalid image returns proper error
- [ ] Missing file returns 400
- [ ] API errors show descriptive messages
- [ ] Timeout handling works

### Dependencies
- [ ] Works without SAM model installed
- [ ] Works without Roboflow credentials
- [ ] Works without LLM API key
- [ ] Fallbacks activate gracefully

---

## Frontend Testing

### UI Components
- [ ] Header displays correctly
- [ ] Upload area is visible
- [ ] Buttons are clickable
- [ ] Health status badge shows

### Image Upload
- [ ] Drag & drop works
- [ ] Click to select works
- [ ] File preview shows
- [ ] Only images accepted
- [ ] Image preview updates

### Analysis
- [ ] "Analyze Image" button works
- [ ] Loading spinner shows during analysis
- [ ] Results display after analysis
- [ ] All score sections visible
- [ ] Summary text displays

### Results Display
- [ ] Nutrition Score shows
- [ ] Mantle Score shows
- [ ] Jaggedness Score shows
- [ ] Redness Analysis shows
- [ ] White Coating shows percentage
- [ ] Papillae Analysis shows counts
- [ ] Crack Detection shows score
- [ ] AI Summary displays

### Error Handling
- [ ] Shows error if image invalid
- [ ] Shows error if upload fails
- [ ] Toast notifications appear
- [ ] Error messages are clear

### Responsive Design
- [ ] Desktop layout (1920x1080)
- [ ] Tablet layout (768x1024)
- [ ] Mobile layout (375x667)
- [ ] Text readable on all sizes
- [ ] Buttons accessible on mobile

### Navigation
- [ ] "Analyze Another Image" resets form
- [ ] Clear button works
- [ ] Can upload new image after analysis

---

## Integration Testing

### API Communication
- [ ] Frontend connects to backend
- [ ] Image successfully uploaded
- [ ] Response parsed correctly
- [ ] Results displayed accurately

### CORS
- [ ] No CORS errors in console
- [ ] Requests succeed
- [ ] Headers correct

### Data Flow
- [ ] Image → Upload → Backend → Frontend
- [ ] Results → API Response → Display
- [ ] All fields populated correctly

---

## Performance Testing

### Speed
- [ ] Backend responds < 2 seconds
- [ ] Frontend loads < 3 seconds
- [ ] Image upload < 30 seconds
- [ ] Results display < 1 second

### Load
- [ ] Multiple uploads work
- [ ] No memory leaks
- [ ] Browser stays responsive

---

## Browser Compatibility

### Chrome
- [ ] Latest version
- [ ] All features work
- [ ] No console errors

### Firefox
- [ ] Latest version
- [ ] All features work
- [ ] No console errors

### Safari
- [ ] Latest version
- [ ] All features work
- [ ] No console errors

### Edge
- [ ] Latest version
- [ ] All features work
- [ ] No console errors

---

## Security Testing

### Input Validation
- [ ] File size limits enforced
- [ ] File type validation works
- [ ] No XSS vulnerabilities
- [ ] API keys not exposed

### API Security
- [ ] CORS properly configured
- [ ] No sensitive data in logs
- [ ] Error messages don't leak info

---

## Accessibility Testing

### Keyboard Navigation
- [ ] Tab key navigates form
- [ ] Enter key submits
- [ ] Escape key clears
- [ ] No keyboard traps

### Screen Reader
- [ ] Headings marked properly
- [ ] Buttons labeled
- [ ] Images have alt text
- [ ] Form inputs labeled

### Color Contrast
- [ ] Text readable on background
- [ ] Score bars distinguishable
- [ ] Status indicators clear

---

## Edge Cases

### Image Handling
- [ ] Very large images (10MB+)
- [ ] Very small images (< 1KB)
- [ ] Unsupported formats (BMP, etc.)
- [ ] Corrupted image files

### Network
- [ ] Slow internet simulation
- [ ] Network timeout handling
- [ ] Backend offline handling
- [ ] Reconnection after failure

### Data
- [ ] Missing analysis fields
- [ ] Zero values in results
- [ ] Very large score values
- [ ] Special characters in summary

---

## Final Checklist

- [ ] All tests passed
- [ ] No console errors
- [ ] No warning messages
- [ ] Documentation complete
- [ ] User can upload image
- [ ] User sees results
- [ ] System is responsive
- [ ] Fallbacks work
- [ ] Error messages helpful
- [ ] Ready for production

---

## Known Limitations

- SAM model optional (uses fallback)
- Roboflow API optional
- Gemini API optional
- Image processing limited without GPU
- Papillae detection may vary by image quality

---

## Notes

Record any issues found:
1. Issue: [describe]
   Status: [open/resolved]
   Fix: [details]

2. Issue: [describe]
   Status: [open/resolved]
   Fix: [details]
