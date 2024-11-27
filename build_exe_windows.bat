@echo off

:: Check if PyInstaller is installed
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo PyInstaller is not installed. Install it with 'pip install pyinstaller'.
    exit /b 1
)

:: Build the executable for Windows
pyinstaller --onefile --name py_executable src\py_executable\main.py

:: Clean up unnecessary build files
rd /s /q build
del py_executable.spec

echo Windows executable built successfully. Find it in the 'dist\' directory.
