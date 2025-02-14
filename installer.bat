@echo off
echo Verifying Python installation...
python --version
if errorlevel 1 (
    echo Error: Python is not installed or is not in PATH
    echo Download Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Installing dependencies...
python -m pip install selenium requests colorama

if errorlevel 1 (
    echo Error installing
    pause
    exit /b 1
)

echo All dependencies were installed correctly!
pause