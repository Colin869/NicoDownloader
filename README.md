# 🎬 NicoNico Video Downloader

A modern, user-friendly application for downloading videos from NicoNico (ニコニコ動画) with a beautiful dark-themed GUI.

## ✨ Features

- 🎥 **Video Downloading** - Download videos from NicoNico with quality options
- 🖥️ **Modern GUI** - Beautiful dark theme built with CustomTkinter
- 📁 **Download Management** - Queue system and progress tracking
- 🔄 **Retry Mechanism** - Automatic retry on failures
- 📚 **History Tracking** - Download history and logs
- ⚙️ **Settings** - Persistent configuration
- 🚀 **Executable Building** - Create standalone .exe files

## 🚀 Quick Start

### Option 1: Run with Python
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Build Executable
```bash
# Build standalone executable
MAKE_EXE.bat
```

### Option 3: Direct Launcher
```bash
# Use the Windows launcher
RUN_DIRECT.bat
```

## 📋 Requirements

- Python 3.8+
- Windows 10/11 (for executable builds)
- Internet connection for video downloads

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/niconico-downloader.git
   cd niconico-downloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

1. **Launch the application**
2. **Enter a NicoNico video URL** (full URL or short nico.ms format)
3. **Select quality** (720p, 480p, 360p, best, worst)
4. **Choose download location**
5. **Click Download** and monitor progress

## 🛠️ Building Executables

### Using the Batch File (Recommended)
```bash
MAKE_EXE.bat
```

### Manual Build
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed main.py
```

## 📁 Project Structure

```
niconico-downloader/
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── MAKE_EXE.bat        # Executable builder
├── RUN_DIRECT.bat      # Direct launcher
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## 🎯 Supported Video Formats

- **Quality Options**: 720p, 480p, 360p, best, worst
- **URL Formats**: Full NicoNico URLs and short nico.ms links
- **Output**: MP4 format with best available quality

## 🐛 Troubleshooting

### Common Issues

1. **"Ordinal 380" DLL Error**
   - Use `MAKE_EXE.bat` to rebuild the executable
   - The `--onedir` build method resolves DLL dependency issues

2. **Application Not Starting**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

3. **Download Failures**
   - Verify internet connection
   - Check if the video URL is valid and accessible
   - Try different quality settings

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are properly installed
3. Try rebuilding the executable with `MAKE_EXE.bat`

---

**Happy downloading!** 🎬✨
