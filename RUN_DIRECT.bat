@echo off
title NicoNico Video Downloader - Direct Launcher
color 0E

echo.
echo ================================================================
echo           NicoNico Video Downloader
echo           Direct Python Launcher
echo ================================================================
echo.
echo This launcher runs the Python script directly without
echo needing to build an executable file.
echo.
echo Benefits:
echo - No build errors or compatibility issues
echo - Always up-to-date with latest changes
echo - Smaller file size
echo - Works on all Windows versions
echo.
echo Requirements:
echo - Python must be installed
echo - Dependencies must be installed
echo.
echo Press any key to start the application...
pause >nul

echo.
echo Starting NicoNico Video Downloader...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo Checking dependencies...
python -c "import customtkinter, yt_dlp, requests, PIL" 2>nul
if errorlevel 1 (
    echo.
    echo Installing missing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies
        echo Please run: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Dependencies OK! Starting application...
echo.

REM Start the application
python main.py

echo.
echo Application closed.
pause
