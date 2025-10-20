@echo off
echo Creating K-Lock Professional Portable Package...
echo.

REM Create portable package directory
if not exist "K-Lock_Portable" mkdir "K-Lock_Portable"
if not exist "K-Lock_Portable\dist" mkdir "K-Lock_Portable\dist"

REM Copy main executable
copy "dist\K-Lock Professional.exe" "K-Lock_Portable\dist\"
if errorlevel 1 (
    echo ERROR: Failed to copy main executable
    pause
    exit /b 1
)

REM Copy icon file
copy "k_lock_icon.ico" "K-Lock_Portable\"
if errorlevel 1 (
    echo ERROR: Failed to copy icon file
    pause
    exit /b 1
)

REM Copy documentation
copy "README.md" "K-Lock_Portable\"
copy "BUILD_INFO.md" "K-Lock_Portable\"

REM Create launcher script
echo @echo off > "K-Lock_Portable\Run_K-Lock.bat"
echo echo Starting K-Lock Professional... >> "K-Lock_Portable\Run_K-Lock.bat"
echo cd /d "%%~dp0" >> "K-Lock_Portable\Run_K-Lock.bat"
echo start "" "dist\K-Lock Professional.exe" >> "K-Lock_Portable\Run_K-Lock.bat"
echo echo K-Lock Professional is starting... >> "K-Lock_Portable\Run_K-Lock.bat"

REM Create system requirements file
echo K-Lock Professional - System Requirements > "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo ========================================== >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo. >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo Operating System: Windows 10/11 (64-bit recommended) >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo RAM: 50 MB available memory >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo Disk Space: 15 MB free space >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo Python: NOT REQUIRED (included in EXE) >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo Dependencies: NOT REQUIRED (included in EXE) >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo. >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo Features: >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo - File and folder lock detection >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo - Process identification and management >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo - Force lock release functionality >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo - Professional GUI with modern design >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"
echo - Standalone executable (no installation required) >> "K-Lock_Portable\SYSTEM_REQUIREMENTS.txt"

REM Create quick start guide
echo K-Lock Professional - Quick Start Guide > "K-Lock_Portable\QUICK_START.txt"
echo ====================================== >> "K-Lock_Portable\QUICK_START.txt"
echo. >> "K-Lock_Portable\QUICK_START.txt"
echo HOW TO USE: >> "K-Lock_Portable\QUICK_START.txt"
echo 1. Double-click "Run_K-Lock.bat" to start the application >> "K-Lock_Portable\QUICK_START.txt"
echo    OR >> "K-Lock_Portable\QUICK_START.txt"
echo    Navigate to "dist" folder and double-click "K-Lock Professional.exe" >> "K-Lock_Portable\QUICK_START.txt"
echo. >> "K-Lock_Portable\QUICK_START.txt"
echo 2. Select a file or folder to analyze: >> "K-Lock_Portable\QUICK_START.txt"
echo    - Click "Browse File" for specific files >> "K-Lock_Portable\QUICK_START.txt"
echo    - Click "Browse Folder" for directories >> "K-Lock_Portable\QUICK_START.txt"
echo    - Or manually enter the path >> "K-Lock_Portable\QUICK_START.txt"
echo. >> "K-Lock_Portable\QUICK_START.txt"
echo 3. Click "Analyze Lock Status" to check for locks >> "K-Lock_Portable\QUICK_START.txt"
echo. >> "K-Lock_Portable\QUICK_START.txt"
echo 4. If locks are detected: >> "K-Lock_Portable\QUICK_START.txt"
echo    - Review the locking processes >> "K-Lock_Portable\QUICK_START.txt"
echo    - Click "Force Release Lock" if needed >> "K-Lock_Portable\QUICK_START.txt"
echo    - Confirm the operation (WARNING: This will close applications) >> "K-Lock_Portable\QUICK_START.txt"
echo. >> "K-Lock_Portable\QUICK_START.txt"
echo SAFETY NOTES: >> "K-Lock_Portable\QUICK_START.txt"
echo - Always save your work before force-releasing locks >> "K-Lock_Portable\QUICK_START.txt"
echo - Some system processes cannot be terminated >> "K-Lock_Portable\QUICK_START.txt"
echo - Run as Administrator if you get access denied errors >> "K-Lock_Portable\QUICK_START.txt"

echo.
echo SUCCESS: K-Lock Professional Portable Package created!
echo Location: K-Lock_Portable\
echo.
echo Package Contents:
dir "K-Lock_Portable" /b
echo.
echo Ready for distribution! The package can run on any Windows machine.
pause
