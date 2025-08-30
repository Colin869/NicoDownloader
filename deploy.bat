@echo off
echo ========================================
echo   DEPLOYING TO GITHUB
echo ========================================
echo.

echo [1/3] Checking Git status...
git status
echo.

echo [2/3] Adding all files...
git add .
echo ✓ Files added

echo.
echo [3/3] Committing changes...
git commit -m "Clean repository structure - remove unnecessary files"
echo ✓ Changes committed

echo.
echo 🎉 Ready to push to GitHub!
echo.
echo Next steps:
echo 1. git push origin main
echo 2. Or use: git push origin master
echo.
pause
