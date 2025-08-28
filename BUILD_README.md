# 🚀 Create Your One-Click NicoNico Downloader

## Quick Start - One Click Build!

### **Option 1: Super Simple (Recommended)**
1. **Double-click** `MAKE_EXE.bat`
2. **Wait** 5-10 minutes for the build to complete
3. **Done!** Your .exe file will be in the `dist` folder

### **Option 2: Manual Build**
1. **Double-click** `BUILD_EXE.bat`
2. **Follow** the on-screen instructions
3. **Wait** for the build to complete

## What You'll Get

After building, you'll have:
- 📁 `dist\NicoNicoDownloader.exe` - Your one-click application
- 🎯 **No Python needed** - Runs on any Windows computer
- 📦 **Everything included** - All dependencies bundled inside
- 🖱️ **Just double-click** to run!

## File Size

The final .exe will be approximately:
- **Size**: 50-100 MB (depending on your system)
- **Reason**: Includes Python runtime + all libraries
- **Benefit**: Works on computers without Python installed

## First Run

- **First launch** may take 10-30 seconds
- **Windows Defender** may show a security warning
- **Click "More info" → "Run anyway"** to continue
- **Subsequent runs** will be much faster

## Troubleshooting

### Build Fails?
- Make sure Python is installed
- Run `pip install pyinstaller` manually
- Check that all dependencies are installed

### .exe Won't Run?
- Try running as Administrator
- Check Windows Defender settings
- Ensure the file wasn't corrupted during download

## What Happens During Build

1. **Installs PyInstaller** (if needed)
2. **Creates custom icon** for the app
3. **Bundles all code** into single executable
4. **Optimizes file size** by excluding unused modules
5. **Creates final .exe** in `dist` folder

## After Building

- **Copy** the .exe file anywhere you want
- **Share** with friends (they don't need Python!)
- **Run** on any Windows 10/11 computer
- **Enjoy** your portable NicoNico downloader!

---

**Note**: The build process creates temporary files in `build` and `__pycache__` folders. You can delete these after successful build.
