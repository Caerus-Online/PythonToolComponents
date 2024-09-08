@echo off
setlocal enabledelayedexpansion

rem --- Configuration ---
set GIT_INSTALLER_URL=https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.2/Git-2.42.0.2-64-bit.exe

rem --- Check if Git is installed ---
where git >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Installing Git now...

    rem --- Download Git installer ---
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%GIT_INSTALLER_URL%', 'GitInstaller.exe')"

    rem --- Install Git silently ---
    start /wait "" GitInstaller.exe /SILENT

    echo Git installation complete!
)

rem --- Check if pip is installed ---
pip --version >nul 2>&1
if errorlevel 1 (
    echo Pip is not installed. Installing pip now...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

rem --- Upgrade pip to the latest version ---
python -m pip install --upgrade pip

rem --- Install required modules ---
pip install PyQt5 pandas plyer

echo Installation complete!
pause