# NicoNico Video Downloader Launcher
Write-Host "Starting NicoNico Video Downloader..." -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "Error: Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if dependencies are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
try {
    python -c "import customtkinter, yt_dlp" 2>$null
    Write-Host "Dependencies found!" -ForegroundColor Green
} catch {
    Write-Host "Dependencies not found. Installing..." -ForegroundColor Yellow
    try {
        pip install -r requirements.txt
        Write-Host "Dependencies installed successfully!" -ForegroundColor Green
    } catch {
        Write-Host "Failed to install dependencies. Please run: pip install -r requirements.txt" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "Launching application..." -ForegroundColor Green
Write-Host ""

# Launch the application
try {
    python main.py
} catch {
    Write-Host "Error launching application: $($_.Exception.Message)" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
