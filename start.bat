@echo off
echo Starting Tongue Analysis System...
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv and start backend
echo Starting Backend Server...
call venv\Scripts\activate.bat
start cmd /k "cd /d %cd% && python -m uvicorn FastApiServer:app --host 0.0.0.0 --port 8000 --reload"

REM Wait a moment for backend to start
timeout /t 2 /nobreak

REM Start frontend
if exist "frontend\node_modules" (
    echo Starting Frontend...
    start cmd /k "cd /d %cd%\frontend && npm start"
) else (
    echo Installing frontend dependencies first...
    start cmd /k "cd /d %cd%\frontend && npm install && npm start"
)

echo.
echo System is starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
pause
