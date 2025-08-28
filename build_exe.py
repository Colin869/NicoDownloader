#!/usr/bin/env python3
"""
Build script to create a single Windows executable for NicoNico Video Downloader
"""

import os
import sys
import subprocess
import shutil

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller found")
        return True
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install PyInstaller")
            return False

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building NicoNico Video Downloader executable...")
    
    # PyInstaller command with optimized settings
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name=NicoNicoDownloader",    # Executable name
        "--icon=icon.ico",              # Icon (if available)
        "--add-data=requirements.txt;.", # Include requirements
        "--hidden-import=customtkinter",
        "--hidden-import=tkinter",
        "--hidden-import=requests",
        "--hidden-import=yt_dlp",
        "--hidden-import=PIL",
        "--hidden-import=json",
        "--hidden-import=threading",
        "--hidden-import=subprocess",
        "--hidden-import=os",
        "--hidden-import=re",
        "--hidden-import=time",
        "--hidden-import=datetime",
        "--hidden-import=urllib.parse",
        "--clean",                      # Clean build cache
        "--noconfirm",                  # Don't ask for confirmation
        "main.py"
    ]
    
    try:
        print("Running PyInstaller...")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_icon():
    """Create a simple icon file if none exists"""
    if not os.path.exists("icon.ico"):
        print("Creating default icon...")
        try:
            # Create a simple text-based icon using PIL
            from PIL import Image, ImageDraw, ImageFont
            
            # Create a 256x256 image with a dark background
            img = Image.new('RGBA', (256, 256), (45, 45, 45, 255))
            draw = ImageDraw.Draw(img)
            
            # Try to use a default font, fall back to basic drawing if no font
            try:
                # Draw a simple "N" symbol
                draw.rectangle([80, 60, 176, 196], outline=(0, 150, 255, 255), width=8)
                draw.rectangle([100, 80, 156, 176], fill=(0, 150, 255, 128))
                draw.text((128, 220), "NicoNico", fill=(255, 255, 255, 255), anchor="mm")
            except:
                # Fallback: simple geometric shapes
                draw.rectangle([80, 60, 176, 196], outline=(0, 150, 255, 255), width=8)
                draw.rectangle([100, 80, 156, 176], fill=(0, 150, 255, 128))
            
            # Save as ICO
            img.save("icon.ico", format='ICO')
            print("✓ Icon created successfully")
        except Exception as e:
            print(f"⚠ Could not create icon: {e}")
            # Remove icon reference from PyInstaller command
            return False
    return True

def create_launcher_bat():
    """Create a simple launcher batch file"""
    launcher_content = """@echo off
echo Starting NicoNico Video Downloader...
echo.
echo If this is your first time running, Windows may show a security warning.
echo Click "More info" and then "Run anyway" to continue.
echo.
pause
start "" "NicoNicoDownloader.exe"
"""
    
    with open("Launch_NicoNicoDownloader.bat", "w") as f:
        f.write(launcher_content)
    print("✓ Launcher batch file created")

def main():
    """Main build process"""
    print("=" * 50)
    print("NicoNico Video Downloader - Executable Builder")
    print("=" * 50)
    
    # Check if PyInstaller is available
    if not check_pyinstaller():
        print("\nPlease install PyInstaller manually:")
        print("pip install pyinstaller")
        return False
    
    # Create icon if needed
    has_icon = create_icon()
    
    # Build the executable
    if build_executable():
        print("\n" + "=" * 50)
        print("BUILD SUCCESSFUL!")
        print("=" * 50)
        
        # Check if executable was created
        exe_path = os.path.join("dist", "NicoNicoDownloader.exe")
        if os.path.exists(exe_path):
            print(f"✓ Executable created: {exe_path}")
            print(f"✓ File size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
            
            # Create launcher
            create_launcher_bat()
            
            print("\n🎉 Your one-click NicoNico Downloader is ready!")
            print("\nTo use:")
            print("1. Double-click 'NicoNicoDownloader.exe' in the 'dist' folder")
            print("2. Or use 'Launch_NicoNicoDownloader.bat' for easier launching")
            print("\nNote: The first run may take a moment as Windows extracts the files.")
            
            return True
        else:
            print("✗ Executable not found in dist folder")
            return False
    else:
        print("\nBuild failed. Please check the error messages above.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("\nPress Enter to exit...")
        input()
    sys.exit(0 if success else 1)
