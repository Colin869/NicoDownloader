@echo off
echo ========================================
echo NicoNico Video Downloader - Installer
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found!
python --version

echo.
echo Installing required packages...
echo This may take a few minutes...
echo.

pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install some packages
    echo Trying alternative installation method...
    echo.
    
    pip install requests yt-dlp customtkinter Pillow
    
    if errorlevel 1 (
        echo.
        echo ERROR: Installation failed. Please check your internet connection
        echo and try running: pip install -r requirements.txt manually
        pause
        exit /b 1
    )
)

echo.
echo Testing installation...
python test_app.py

if errorlevel 1 (
    echo.
    echo WARNING: Some tests failed. The application may not work correctly.
    echo Please check the error messages above.
) else (
    echo.
    echo ========================================
    echo Installation completed successfully!
    echo ========================================
    echo.
    echo You can now run the application with:
    echo   python main.py
    echo.
    echo Or use the provided batch files:
    echo   run_downloader.bat
    echo.
)

echo.
echo Press any key to exit...
pause >nul
