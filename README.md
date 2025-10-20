# K-Lock Professional

**Advanced File & Folder Lock Manager for Windows**

K-Lock Professional is a powerful Windows application that helps you identify and manage file and folder locks. Whether you're dealing with locked files that prevent deletion, modification, or access, K-Lock provides comprehensive analysis and force-release capabilities.

## Quick Start

### Download & Run (Recommended)
1. Go to the [Releases](https://github.com/naderlb/k-lock/releases) page
2. Download `K-Lock Professional.exe` from the releases folder
3. Run the executable directly - no installation required!

### From Source
1. **Prerequisites:**
   - Windows 10/11
   - Python 3.7 or higher

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run K-Lock:**
   ```bash
   python file_lock_checker.py
   ```

## Features

- **Comprehensive Lock Analysis** - Detect which processes are locking files or folders
- **File & Folder Support** - Works with both individual files and entire directories
- **Force Release** - Terminate locking processes to release locks (with safety warnings)
- **Professional UI** - Modern, intuitive interface with real-time status updates
- **Detailed Reports** - Get comprehensive information about locking processes
- **Real-time Monitoring** - Refresh analysis to track lock status changes
- **Advanced Detection** - Multiple methods to identify locking processes
- **Safety Features** - Confirmation dialogs and data loss warnings

## Usage

### Basic Operation

1. **Launch K-Lock Professional**
2. **Select Target:**
   - Click "Browse File" to select a specific file
   - Click "Browse Folder" to select a directory
   - Or manually enter the path in the text field

3. **Analyze Lock Status:**
   - Click "Analyze Lock Status" to check for locks
   - View detailed analysis report in the results panel

4. **Release Locks (if needed):**
   - If locks are detected, click "Force Release Lock"
   - Confirm the operation (WARNING: This will close applications)
   - K-Lock will terminate the locking processes

### Understanding the Results

**Locked Status:**
- Shows which processes are using the file/folder
- Displays Process ID (PID), name, executable path, and command line
- Provides option to force release the lock

**Unlocked Status:**
- Confirms the file/folder is accessible
- Safe to perform operations on the target

## Safety Features

- **Confirmation Dialogs** - Always asks before terminating processes
- **Process Information** - Shows exactly which applications will be closed
- **Data Loss Warnings** - Alerts about potential unsaved work
- **Error Handling** - Graceful handling of access denied or system processes

## Technical Details

- Uses Windows API for low-level file access detection
- Leverages `psutil` for process enumeration and management
- Threaded operations to prevent UI freezing
- Professional error reporting and user feedback

## System Requirements

- **OS:** Windows 10/11 (64-bit recommended)
- **Python:** 3.7+
- **Dependencies:** psutil
- **Permissions:** May require administrator privileges for some operations

## Troubleshooting

**"Access Denied" Errors:**
- Run K-Lock as Administrator
- Some system processes cannot be terminated

**No Processes Found:**
- The file may be locked by system-level processes
- Try running as Administrator
- Check if the file is in use by Windows services

**Application Won't Start:**
- For EXE version: Ensure Windows 10/11 compatibility
- For source version: Ensure Python 3.7+ is installed
- Install required dependencies: `pip install -r requirements.txt`

## Download

**Ready-to-Use Executable:**
- Download `K-Lock Professional.exe` from the [Releases](https://github.com/naderlb/k-lock/releases) page
- No installation required - just download and run!
- File size: 10.0 MB (includes all dependencies)

## License

This project is provided as-is for educational and professional use.

## Support

For issues or questions, please check the troubleshooting section above or review the error messages in the application.
