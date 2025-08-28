#!/usr/bin/env python3
"""
Simple test script for NicoNico Video Downloader
Tests basic functionality without requiring actual downloads
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import tkinter
        print("✓ tkinter imported successfully")
    except ImportError as e:
        print(f"✗ tkinter import failed: {e}")
        return False
    
    try:
        import customtkinter
        print("✓ customtkinter imported successfully")
    except ImportError as e:
        print(f"✗ customtkinter import failed: {e}")
        return False
    
    try:
        import requests
        print("✓ requests imported successfully")
    except ImportError as e:
        print(f"✗ requests import failed: {e}")
        return False
    
    try:
        import yt_dlp
        print("✓ yt-dlp imported successfully")
    except ImportError as e:
        print(f"✗ yt-dlp import failed: {e}")
        return False
    
    return True

def test_ytdlp():
    """Test if yt-dlp is working"""
    try:
        import subprocess
        result = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ yt-dlp version: {result.stdout.strip()}")
            return True
        else:
            print(f"✗ yt-dlp check failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ yt-dlp test failed: {e}")
        return False

def test_gui_creation():
    """Test if GUI can be created (without showing it)"""
    try:
        import customtkinter as ctk
        ctk.set_appearance_mode("dark")
        
        # Create window but don't show it
        root = ctk.CTk()
        root.withdraw()  # Hide the window
        
        # Test basic widget creation
        frame = ctk.CTkFrame(root)
        label = ctk.CTkLabel(frame, text="Test")
        button = ctk.CTkButton(frame, text="Test")
        
        root.destroy()
        print("✓ GUI creation test passed")
        return True
    except Exception as e:
        print(f"✗ GUI creation test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("NicoNico Video Downloader - System Test")
    print("=" * 40)
    
    tests = [
        ("Module Imports", test_imports),
        ("yt-dlp Check", test_ytdlp),
        ("GUI Creation", test_gui_creation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning: {test_name}")
        print("-" * 20)
        if test_func():
            passed += 1
        else:
            print(f"Test '{test_name}' failed!")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The application should work correctly.")
        return True
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
