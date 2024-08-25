@echo off
cls
title <RE-DACT> - Redaction Tool


setlocal enabledelayedexpansion

echo.
echo "   ___ ________  _______                  ________  ________  ________ _________  ___     "
echo "   /  /|\   __  \|\  ___ \                |\   ___ \|\   __  \|\   ____\\___   ___\\  \   "
echo "  /  / | \  \|\  \ \   __/|   ____________\ \  \_|\ \ \  \|\  \ \  \___\|___ \  \_\ \  \  "
echo " /  / / \ \   _  _\ \  \_|/__|\____________\ \  \ \\ \ \   __  \ \  \       \ \  \ \ \  \ "
echo "|\  \/   \ \  \\  \\ \  \_|\ \|____________|\ \  \_\\ \ \  \ \  \ \  \____   \ \  \ \/  /|"
echo "\ \  \    \ \__\\ _\\ \_______\              \ \_______\ \__\ \__\ \_______\  \ \__\/  // "
echo " \ \__\    \|__|\|__|\|_______|               \|_______|\|__|\|__|\|_______|   \|__/_ //  "
echo "  \|__|                                                                           |__|/   "
echo.
echo "==============================================================="
echo "            < R E - D A C T >                 "
echo "==============================================================="
echo.
timeout /t 1 >nul

:: Activate the virtual environment
if exist env\Scripts\activate (
    call env\Scripts\activate
    echo Virtual environment activated successfully.
) else (
    echo Error: Virtual environment not found. Please ensure the path is correct.
    pause
    exit /b
)

:: Starting Flask server
echo Starting Flask server...
timeout /t 1 >nul
python -m flask run

if errorlevel 1 (
    echo [Error] Failed to start Flask server. Please check the error messages above.
    pause
    exit /b
)

:: End
pause
