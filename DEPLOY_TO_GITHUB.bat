@echo off
title Deploy to GitHub - NicoNico Downloader
color 0D

echo.
echo ================================================================
echo           DEPLOY TO GITHUB
echo           NicoNico Video Downloader
echo ================================================================
echo.
echo This script will help you deploy your project to GitHub.
echo Make sure you have:
echo - Git installed on your system
echo - GitHub account with repository: Colin869/NicoDownloader
echo - All project files ready
echo.
echo Press any key to continue...
pause >nul

echo.
echo [1/6] Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo.
    echo Please install Git from: https://git-scm.com/downloads
    echo Make sure to check "Add Git to PATH" during installation
    echo.
    pause
    exit /b 1
)
echo ✓ Git found: 
git --version

echo.
echo [2/6] Checking current directory...
echo Current directory: %CD%
echo.
echo Make sure this is your project directory containing:
echo - main.py
echo - requirements.txt
echo - README.md
echo - LICENSE
echo.
echo Is this correct? (Y/N)
set /p confirm=
if /i "%confirm%" neq "Y" (
    echo Please navigate to your project directory and run this script again.
    pause
    exit /b 1
)

echo.
echo [3/6] Initializing Git repository...
if not exist ".git" (
    echo Initializing new Git repository...
    git init
) else (
    echo Git repository already exists.
)

echo.
echo [4/6] Adding GitHub remote...
git remote -v | findstr "origin" >nul
if errorlevel 1 (
    echo Adding GitHub remote origin...
    git remote add origin https://github.com/Colin869/NicoDownloader.git
) else (
    echo Remote origin already exists.
)

echo.
echo [5/6] Staging files...
echo Adding all files to Git...
git add .

echo.
echo [6/6] Committing and pushing...
echo.
echo Enter your commit message (or press Enter for default):
set /p commit_msg=
if "%commit_msg%"=="" (
    set commit_msg=🎉 Initial release: NicoNico Video Downloader v1.1.0

✨ Features:
- Download videos from NicoNico with quality options
- Modern dark-themed GUI using CustomTkinter
- Download queue system and cancellation support
- Automatic retry mechanism and download history
- Settings persistence and real-time progress tracking
- Support for full URLs and short URLs (nico.ms)
- Windows executable building with PyInstaller

🚀 Ready for production use!
)

echo.
echo Committing with message:
echo %commit_msg%
echo.
git commit -m "%commit_msg%"

echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ================================================================
    echo                    PUSH FAILED
    echo ================================================================
    echo.
    echo Possible reasons:
    echo - GitHub repository doesn't exist yet
    echo - Authentication failed (check your credentials)
    echo - Network connection issues
    echo.
    echo Please:
    echo 1. Create the repository at: https://github.com/Colin869/NicoDownloader
    echo 2. Ensure you're logged into Git with proper credentials
    echo 3. Try running this script again
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================================
echo                    DEPLOYMENT SUCCESSFUL!
echo ================================================================
echo.
echo 🎉 Your NicoNico Video Downloader is now on GitHub!
echo.
echo Repository: https://github.com/Colin869/NicoDownloader
echo.
echo Next steps:
echo 1. Visit your repository on GitHub
echo 2. Verify all files are uploaded correctly
echo 3. Check that README displays properly
echo 4. Share your project with the community!
echo.
echo Press any key to exit...
pause >nul
