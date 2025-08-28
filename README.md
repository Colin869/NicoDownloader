# 🎬 NicoNico Video Downloader

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](https://github.com/Colin869/NicoDownloader)

A professional, feature-rich video downloader for NicoNico (ニコニコ動画) built with Python and CustomTkinter. Download videos with quality options, download queue management, and a modern dark-themed GUI.

## ✨ Features

### 🎯 Core Functionality
- **Video Download**: Download videos from NicoNico with multiple quality options
- **URL Support**: Full URLs and short URLs (nico.ms) supported
- **Quality Selection**: Choose from 720p, 480p, 360p, or best available
- **Metadata Preservation**: Automatic thumbnail and description download
- **Format Options**: MP4, WebM, and other supported formats

### 🚀 Advanced Features
- **Download Queue**: Queue multiple videos for sequential downloading
- **Download Cancellation**: Cancel downloads in progress
- **Retry Mechanism**: Automatic retry up to 3 times on failure
- **Download History**: Track and view download history
- **Settings Persistence**: Remember your preferences between sessions
- **Real-time Progress**: Live progress tracking with speed and ETA

### 🖥️ User Experience
- **Modern GUI**: Beautiful dark-themed interface using CustomTkinter
- **Responsive Design**: Non-blocking downloads with background processing
- **Error Handling**: Comprehensive error messages and recovery options
- **Log Management**: Detailed logging with clear functions
- **Cross-Platform**: Works on Windows 10/11

## 🚀 Quick Start

### Option 1: Run Directly (Recommended)
1. **Clone the repository**
   ```bash
   git clone https://github.com/Colin869/NicoDownloader.git
   cd NicoDownloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Option 2: Windows Executable
1. **Double-click** `MAKE_EXE.bat` to build the executable
2. **Wait** 5-10 minutes for the build to complete
3. **Find** your `.exe` file in the `dist` folder
4. **Double-click** to run (no Python needed!)

### Option 3: Direct Launcher
- **Double-click** `RUN_DIRECT.bat` for instant launch
- Automatically checks dependencies and starts the app

## 📋 Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11
- **Dependencies**: See `requirements.txt`

## 🛠️ Installation

### Prerequisites
1. **Install Python 3.8+** from [python.org](https://www.python.org/downloads/)
2. **Ensure pip is available** (usually included with Python)

### Dependencies
```bash
pip install -r requirements.txt
```

### Manual Installation
```bash
pip install customtkinter>=5.2.0
pip install yt-dlp>=2023.12.30
pip install requests>=2.31.0
pip install Pillow>=10.1.0
```

## 🎮 Usage

1. **Launch** the application
2. **Paste** a NicoNico video URL (full or short)
3. **Select** your preferred quality
4. **Choose** download location
5. **Click** "Download Video"
6. **Monitor** progress in real-time
7. **Enjoy** your downloaded video!

### Supported URL Formats
- Full URLs: `https://www.nicovideo.jp/watch/sm12345678`
- Short URLs: `https://nico.ms/sm12345678`
- Video IDs: `sm12345678`

## 🔧 Troubleshooting

### Common Issues

#### Build Errors (Ordinal 380, etc.)
- **Solution 1**: Use `BUILD_ROBUST.bat` for compatibility fixes
- **Solution 2**: Install [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- **Solution 3**: Run as Administrator
- **Solution 4**: Use Python script directly (`python main.py`)

#### Import Errors
```bash
pip install -r requirements.txt
```

#### GUI Issues
- Ensure CustomTkinter is properly installed
- Try running in console mode if windowed mode fails

### Getting Help
1. Check the [Issues](https://github.com/Colin869/NicoDownloader/issues) page
2. Review the [CHANGELOG.md](CHANGELOG.md) for known issues
3. Try the alternative launchers provided

## 📁 Project Structure

```
NicoDownloader/
├── 🎯 Core Application
│   ├── main.py                    # Main application (GUI + Logic)
│   ├── test_app.py               # System testing script
│   └── requirements.txt          # Python dependencies
│
├── 🚀 Executable Building
│   ├── MAKE_EXE.bat             # ⭐ One-click build (Recommended!)
│   ├── BUILD_ROBUST.bat         # Robust build with error handling
│   ├── BUILD_EXE.bat            # Alternative build script
│   ├── build_exe.py             # Python build automation
│   └── NicoNicoDownloader.spec  # PyInstaller configuration
│
├── 🛠️ Alternative Launchers
│   ├── RUN_DIRECT.bat           # Direct Python launcher
│   ├── run_downloader.bat       # Windows launcher
│   └── run_downloader.ps1       # PowerShell launcher
│
├── 📚 Documentation
│   ├── CHANGELOG.md             # Version history
│   ├── PROJECT_SUMMARY.md       # Technical overview
│   ├── BUILD_README.md          # Build instructions
│   └── QUICK_START.md           # Quick start guide
│
└── ⚙️ Configuration
    └── config_example.json      # Settings template
```

## 🏗️ Building from Source

### Prerequisites
- Python 3.8+
- PyInstaller
- All dependencies installed

### Build Commands
```bash
# Standard build
pyinstaller --onefile --windowed --name=NicoNicoDownloader main.py

# With custom icon
pyinstaller --onefile --windowed --name=NicoNicoDownloader --icon=icon.ico main.py

# Maximum compatibility
pyinstaller --onefile --name=NicoNicoDownloader --hidden-import=customtkinter --hidden-import=tkinter main.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **yt-dlp**: Core video downloading functionality
- **CustomTkinter**: Modern GUI framework
- **NicoNico**: Video platform support
- **Python Community**: Open source tools and libraries

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/Colin869/NicoDownloader/issues)
- **Discussions**: [Join the community](https://github.com/Colin869/NicoDownloader/discussions)

## 🎉 What's New

### Version 1.1.0 (Latest)
- ✨ Download queue system
- ❌ Download cancellation support
- 🔁 Automatic retry mechanism
- 📚 Download history tracking
- ⚙️ Settings persistence
- 📊 Enhanced progress tracking
- 🖼️ Video information preview
- 🛡️ Improved error handling

### Version 1.0.0
- 🎥 Basic video downloading
- 🖥️ Modern GUI interface
- 🔍 URL validation and support
- 🎨 Quality selection options

---

**⭐ Star this repository if you find it useful!**

**Happy downloading!** 🎬✨
