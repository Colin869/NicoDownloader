#!/usr/bin/env python3
"""
Simple test script to check if the main application can be created
"""

import sys
import traceback

def test_import():
    """Test if main module can be imported"""
    try:
        import main
        print("✓ Main module imported successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to import main module: {e}")
        traceback.print_exc()
        return False

def test_class_creation():
    """Test if the main class can be created"""
    try:
        import main
        app = main.NicoNicoDownloader()
        print("✓ NicoNicoDownloader class created successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to create NicoNicoDownloader: {e}")
        traceback.print_exc()
        return False

def test_gui_creation():
    """Test if GUI can be created (without showing window)"""
    try:
        import main
        app = main.NicoNicoDownloader()
        
        # Test if all required attributes exist
        required_attrs = [
            'root', 'download_path', 'url_var', 'quality_var', 
            'status_var', 'progress_var', 'progress_bar', 'log_text',
            'cancel_btn', 'download_queue', 'current_download'
        ]
        
        for attr in required_attrs:
            if not hasattr(app, attr):
                print(f"✗ Missing attribute: {attr}")
                return False
        
        print("✓ All required attributes present")
        print("✓ GUI creation test passed")
        return True
        
    except Exception as e:
        print(f"✗ GUI creation failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("NicoNico Video Downloader - Simple Test")
    print("=" * 50)
    
    tests = [
        ("Module Import", test_import),
        ("Class Creation", test_class_creation),
        ("GUI Creation", test_gui_creation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning: {test_name}")
        print("-" * 30)
        
        if test_func():
            passed += 1
            print(f"✓ {test_name} passed")
        else:
            print(f"✗ {test_name} failed")
    
    print(f"\n{'=' * 50}")
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
