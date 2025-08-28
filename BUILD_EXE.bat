@echo off
echo ========================================
echo NicoNico Video Downloader - EXE Builder
echo ========================================
echo.
echo This will create a single clickable .exe file
echo that includes everything needed to run the app.
echo.
echo Building may take several minutes...
echo.
pause

echo.
echo Starting build process...
python build_exe.py

echo.
echo Build process completed!
echo.
echo If successful, you'll find your executable in the 'dist' folder.
echo.
pause
