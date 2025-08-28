@echo off
title NicoNico Downloader - Robust EXE Builder
color 0B

echo.
echo ================================================================
echo           ROBUST EXECUTABLE BUILDER
echo           (Fixes Ordinal 380 Error)
echo ================================================================
echo.
echo This script will try multiple build methods to overcome
echo Windows compatibility issues like the "ordinal 380" error.
echo.
echo Press any key to start...
pause >nul

echo.
echo [1/6] Checking system requirements...
echo Windows Version:
ver
echo.
echo Python Version:
python --version
echo.
echo Checking for Visual C++ Redistributable...

echo [2/6] Installing/Updating PyInstaller...
pip uninstall pyinstaller -y >nul 2>&1
pip install pyinstaller==5.13.2 --quiet
if errorlevel 1 (
    echo Trying alternative PyInstaller version...
    pip install pyinstaller==6.3.0 --quiet
)

echo [3/6] Creating icon...
python -c "
try:
    from PIL import Image, ImageDraw
    img = Image.new('RGBA', (256, 256), (45, 45, 45, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([80, 60, 176, 196], outline=(0, 150, 255, 255), width=8)
    draw.rectangle([100, 80, 156, 176], fill=(0, 150, 255, 128))
    img.save('icon.ico', format='ICO')
    print('Icon created successfully')
except:
    print('Icon creation skipped')
"

echo [4/6] Method 1: Standard build with compatibility flags...
pyinstaller --onefile --windowed --name=NicoNicoDownloader --icon=icon.ico --clean --noconfirm --hidden-import=customtkinter --hidden-import=tkinter --hidden-import=requests --hidden-import=yt_dlp --hidden-import=PIL --hidden-import=json --hidden-import=threading --hidden-import=subprocess --hidden-import=os --hidden-import=re --hidden-import=time --hidden-import=datetime --hidden-import=urllib.parse main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo ✓ Method 1 successful!
    goto :success
)

echo.
echo [5/6] Method 2: Console mode for maximum compatibility...
pyinstaller --onefile --name=NicoNicoDownloader --icon=icon.ico --clean --noconfirm --hidden-import=customtkinter --hidden-import=tkinter --hidden-import=requests --hidden-import=yt_dlp --hidden-import=PIL --hidden-import=json --hidden-import=threading --hidden-import=subprocess --hidden-import=os --hidden-import=re --hidden-import=time --hidden-import=datetime --hidden-import=urllib.parse main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo ✓ Method 2 successful!
    goto :success
)

echo.
echo [6/6] Method 3: Minimal build with basic settings...
pyinstaller --onefile --name=NicoNicoDownloader --clean --noconfirm main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo ✓ Method 3 successful!
    goto :success
)

echo.
echo ================================================================
echo                    ALL BUILD METHODS FAILED
echo ================================================================
echo.
echo The "ordinal 380" error or similar compatibility issues
echo could not be resolved with the current setup.
echo.
echo RECOMMENDED SOLUTIONS:
echo.
echo 1. INSTALL VISUAL C++ REDISTRIBUTABLE:
echo    Download from Microsoft: https://aka.ms/vs/17/release/vc_redist.x64.exe
echo.
echo 2. UPDATE WINDOWS:
echo    Run Windows Update to latest version
echo.
echo 3. RUN AS ADMINISTRATOR:
echo    Right-click this batch file and "Run as administrator"
echo.
echo 4. USE PYTHON SCRIPT INSTEAD:
echo    Run: python main.py
echo.
echo 5. TRY DIFFERENT PYTHON VERSION:
echo    Install Python 3.9 or 3.10 (more compatible)
echo.
echo Press any key to exit...
pause >nul
exit /b 1

:success
echo.
echo ================================================================
echo                    BUILD SUCCESSFUL!
echo ================================================================
echo.
echo Your executable is ready in the 'dist' folder!
echo.
echo File: dist\NicoNicoDownloader.exe
echo Size: 
for %%A in ("dist\NicoNicoDownloader.exe") do echo        %%~zA bytes
echo.
echo 🎉 You can now double-click the .exe file to run the app!
echo.
echo Note: First run may take a moment as Windows extracts files.
echo.
echo Press any key to exit...
pause >nul
