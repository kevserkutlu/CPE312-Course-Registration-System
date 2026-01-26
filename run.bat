@echo off
REM Course Registration System - Fullstack Application Runner (Windows)
REM This script starts the entire application with all necessary components

setlocal enabledelayedexpansion

cls
echo ==================================================
echo.
echo 🎓 Course Registration System
echo.
echo ==================================================
echo.

REM Get the script directory
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo 📁 Working Directory: %SCRIPT_DIR%
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo ⚠️  Virtual environment not found. Creating...
    python -m venv .venv
    echo ✅ Virtual environment created
)

echo.
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

echo ✅ Virtual environment activated
echo.

REM Install/update dependencies
echo 📦 Installing dependencies...
pip install -q -r requirements.txt 2>nul || (
    echo ⚠️  requirements.txt not found or pip install failed
    echo 🔧 Installing Flask and SQLAlchemy...
    pip install -q flask sqlalchemy psycopg2-binary
)
echo ✅ Dependencies installed
echo.

REM Start the Flask web server
echo 🚀 Starting Flask web server...
echo.
echo ════════════════════════════════════════════════
echo ✅ Application is starting!
echo ════════════════════════════════════════════════
echo.
echo 📍 Web Interface: http://localhost:5001
echo.
echo Press CTRL+C to stop the server
echo.

REM Run the Flask application
python web.py

pause
