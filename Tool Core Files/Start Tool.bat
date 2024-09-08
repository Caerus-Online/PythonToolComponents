@echo off

rem --- Configuration ---
set PY_FILE=main.py
set UPDATER_FILE=updater.py

rem Run the updater script first (without opening a cmd window)
pythonw.exe %UPDATER_FILE%

rem Wait for the updater script to finish before running the main script
timeout /t 5 /nobreak >nul  

rem Then run the main script
start pythonw.exe %PY_FILE%