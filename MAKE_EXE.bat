@echo off
title NicoNico Downloader - EXE Builder
color 0A

echo.
echo  ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ██╗██╗ ██████╗ 
echo  ████╗  ██║██║██╔════╝██╔═══██╗████╗  ██║██║██╔═══██╗
echo  ██╔██╗ ██║██║██║     ██║   ██║██╔██╗ ██║██║██║   ██║
echo  ██║╚██╗██║██║██║     ██║   ██║██║╚██╗██║██║██║   ██║
echo  ██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚████║██║╚██████╔╝
echo  ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ 
echo.
echo  ██████╗  ██████╗ ██╗      ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗ 
echo  ██╔══██╗██╔═══██╗██║     ██╔═══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
echo  ██║  ██║██║   ██║██║     ██║   ██║██║   ██║██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
echo  ██║  ██║██║   ██║██║     ██║   ██║██║   ██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
echo  ██████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║
echo  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
echo.
echo ================================================================
echo                    EXECUTABLE BUILDER
echo ================================================================
echo.
echo This will create a single .exe file that you can double-click
echo to run the NicoNico Video Downloader without needing Python!
echo.
echo Building will take 5-10 minutes. Please be patient...
echo.
echo Press any key to start building...
pause >nul

echo.
echo [1/5] Installing PyInstaller...
pip install pyinstaller --quiet

echo [2/5] Creating icon...
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

echo [3/5] Building executable (Method 1 - Standard)...
echo Trying standard build method...
pyinstaller --onefile --windowed --name=NicoNicoDownloader --icon=icon.ico --clean --noconfirm main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo Standard build successful!
    goto :success
)

echo.
echo [4/5] Standard build failed, trying alternative method...
echo Using compatibility mode for Windows...
pyinstaller --onefile --windowed --name=NicoNicoDownloader --icon=icon.ico --clean --noconfirm --hidden-import=customtkinter --hidden-import=tkinter --hidden-import=requests --hidden-import=yt_dlp --hidden-import=PIL main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo Alternative build successful!
    goto :success
)

echo.
echo [5/5] Trying final fallback method...
echo Using console mode for maximum compatibility...
pyinstaller --onefile --name=NicoNicoDownloader --icon=icon.ico --clean --noconfirm --hidden-import=customtkinter --hidden-import=tkinter --hidden-import=requests --hidden-import=yt_dlp --hidden-import=PIL main.py

if exist "dist\NicoNicoDownloader.exe" (
    echo Fallback build successful!
    goto :success
)

echo.
echo ================================================================
echo                    BUILD FAILED
echo ================================================================
echo.
echo All build methods failed. This might be due to:
echo - Windows version compatibility issues
echo - Missing system dependencies
echo - PyInstaller version conflicts
echo.
echo Please try:
echo 1. Update Windows to latest version
echo 2. Run as Administrator
echo 3. Install Visual C++ Redistributable
echo 4. Try the Python script version instead
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
