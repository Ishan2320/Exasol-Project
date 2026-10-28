@echo off
setlocal
cd /d "%~dp0"
echo ==========================================
echo Exasol AI Business Intelligence Assistant
echo ==========================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python launcher "py" was not found. Install Python 3.11 or 3.12 from https://www.python.org/downloads/
  echo During installation, enable "Add Python to PATH".
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating Python virtual environment...
  py -3 -m venv .venv
  if errorlevel 1 (
    echo Could not create the environment. Ensure Python 3 is installed.
    pause
    exit /b 1
  )
)
echo Installing/checking packages. First run may take a few minutes...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
  echo Package installation failed. Check your internet connection and Python installation.
  pause
  exit /b 1
)
echo Starting the app in your browser...
".venv\Scripts\python.exe" -m streamlit run app.py
pause
