@echo off

title Downloads Organizer

cd /d "%~dp0"

echo ============================================
echo DOWNLOADS ORGANIZER
echo ============================================
echo.
echo Starting organizer...
echo.

where python >nul 2>&1

if %errorlevel%==0 (
    python organizer.py
) else (
    where py >nul 2>&1

    if %errorlevel%==0 (
        py organizer.py
    ) else (
        echo.
        echo ERROR: Python was not found.
        echo.
        echo Please install Python 3 and try again.
    )
)

echo.
echo Press any key to close this window.
pause >nul