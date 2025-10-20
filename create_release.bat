@echo off
echo Creating GitHub Release for K-Lock Professional...
echo.

REM Check if GitHub CLI is available
gh --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: GitHub CLI (gh) is not installed or not in PATH
    echo Please install GitHub CLI from: https://cli.github.com/
    echo Or create the release manually on GitHub.com
    pause
    exit /b 1
)

echo GitHub CLI found. Creating release...

REM Create the release
gh release create v1.0.0 "releases/K-Lock Professional.exe" ^
  --title "K-Lock Professional v1.0.0" ^
  --notes "## K-Lock Professional v1.0.0 - Initial Release

### Download
- **K-Lock Professional.exe** (10.0 MB) - Ready to download!
- **System Requirements:** Windows 10/11 (64-bit recommended)
- **Dependencies:** None required (all included in EXE)

### Features
- 🔍 Advanced file and folder lock detection
- 🎯 Process identification with detailed information
- ⚠️ Force release functionality with safety warnings
- 🎨 Professional GUI with real-time updates
- 🛡️ Safety features and confirmation dialogs

### Quick Start
1. Download K-Lock Professional.exe
2. Run the executable (no installation required)
3. Select a file or folder to analyze
4. Click 'Analyze Lock Status'
5. Force release locks if needed

**K-Lock Professional** - The professional solution for file and folder lock management on Windows."

if errorlevel 1 (
    echo ERROR: Failed to create release
    pause
    exit /b 1
)

echo.
echo SUCCESS: GitHub release created!
echo Visit: https://github.com/naderlb/k-lock/releases
echo.
pause
