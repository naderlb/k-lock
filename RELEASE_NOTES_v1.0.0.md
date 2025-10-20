# K-Lock Professional v1.0.0 - Initial Release

## 🎉 First Release!

**K-Lock Professional** is now available as a standalone Windows application for detecting and managing file and folder locks.

## 📦 Download

- **K-Lock Professional.exe** (10.0 MB) - [Download Here](releases/K-Lock%20Professional.exe)
- **System Requirements:** Windows 10/11 (64-bit recommended)
- **Dependencies:** None required (all included in EXE)

## ✨ Features

### 🔍 **Advanced Lock Detection**
- Detects which processes are locking files or folders
- Multiple detection methods for comprehensive analysis
- Works with both individual files and entire directories

### 🎯 **Process Identification**
- Shows Process ID (PID), name, executable path, and command line
- Identifies processes using files inside locked folders
- Detects processes with working directories in locked folders

### ⚠️ **Force Release**
- Safely terminate locking processes to release locks
- Confirmation dialogs with detailed process information
- Data loss warnings before terminating applications

### 🎨 **Professional Interface**
- Modern, intuitive GUI with real-time status updates
- Professional icon and branding
- Detailed analysis reports with timestamps
- Safety features and user-friendly error messages

### 🛡️ **Safety Features**
- Confirmation dialogs before terminating processes
- Clear warnings about potential data loss
- Graceful error handling and user feedback
- Administrator privilege detection

## 🚀 Quick Start

1. **Download** `K-Lock Professional.exe`
2. **Run** the executable (no installation required)
3. **Select** a file or folder to analyze
4. **Click** "Analyze Lock Status"
5. **Review** the detailed report
6. **Force Release** locks if needed (with confirmation)

## 🔧 Technical Details

- **Language:** Python 3.13
- **GUI Framework:** tkinter with custom styling
- **Process Detection:** psutil + Windows API
- **Build Tool:** PyInstaller 6.16.0
- **Icon:** Custom-designed professional lock and key icon
- **Size:** 10.0 MB (includes Python runtime and all dependencies)

## 📋 System Requirements

- **Operating System:** Windows 10/11 (64-bit recommended)
- **Memory:** 50 MB available RAM
- **Disk Space:** 15 MB free space
- **Dependencies:** None (all included in EXE)

## 🐛 Known Issues

- Some system processes cannot be terminated (by design)
- May require Administrator privileges for some operations
- Process detection may not work with all antivirus software

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/naderlb/k-lock/issues)
- **Documentation:** [README.md](README.md)
- **Source Code:** [GitHub Repository](https://github.com/naderlb/k-lock)

---

**K-Lock Professional** - The professional solution for file and folder lock management on Windows.

*Made with ❤️ for Windows users who need reliable file lock management.*
