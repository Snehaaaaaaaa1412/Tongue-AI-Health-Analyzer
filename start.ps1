Write-Host "Starting Tongue Analysis System..." -ForegroundColor Green
Write-Host ""

# Check if venv exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate venv
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Start backend
Write-Host "Starting Backend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList @"
    Set-Location '$pwd'
    python -m uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload
"@ -WindowStyle Normal

# Wait for backend to start
Start-Sleep -Seconds 2

# Start frontend
Write-Host "Starting Frontend..." -ForegroundColor Yellow
if (Test-Path "frontend\node_modules") {
    Start-Process powershell -ArgumentList @"
        Set-Location '$pwd\frontend'
        npm start
"@ -WindowStyle Normal
} else {
    Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
    Start-Process powershell -ArgumentList @"
        Set-Location '$pwd\frontend'
        npm install
        npm start
"@ -WindowStyle Normal
}

Write-Host ""
Write-Host "System is starting..." -ForegroundColor Green
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Windows will open automatically in a few seconds..." -ForegroundColor Green
