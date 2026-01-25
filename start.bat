@echo off
echo ========================================
echo Stylistic False Positive Analyzer (SFP Analyzer)
echo ========================================
echo.
echo Installing dependencies...
call npm install
echo.
echo ========================================
echo Starting development server...
echo Press Ctrl+C to stop the server
echo ========================================
echo.
call npm run dev
