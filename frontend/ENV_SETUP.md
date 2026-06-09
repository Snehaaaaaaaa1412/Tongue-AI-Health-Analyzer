# Frontend Environment Configuration

## Local Development

### .env.local
```
REACT_APP_API_BASE_URL=http://127.0.0.1:8000
REACT_APP_ENV=development
```

### .env.development
```
REACT_APP_API_BASE_URL=http://localhost:8000
REACT_APP_ENV=development
REACT_APP_DEBUG=true
```

### .env.production
```
REACT_APP_API_BASE_URL=https://api.your-domain.com
REACT_APP_ENV=production
REACT_APP_DEBUG=false
```

## Using Environment Variables in Code

```javascript
const API_URL = process.env.REACT_APP_API_BASE_URL;
const IS_DEBUG = process.env.REACT_APP_DEBUG === 'true';
```

## Important Notes

- Only variables prefixed with `REACT_APP_` are exposed to the frontend
- Never store sensitive data (API keys, secrets) in frontend
- `.env.local` takes precedence over `.env`
- Restart dev server after changing `.env` files

## Backend API Configuration

### Development
```
http://127.0.0.1:8000
```

### Production
```
https://api.tongue-analysis.com
```

Update `src/services/api.js` accordingly.
