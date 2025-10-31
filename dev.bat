@echo off
REM Accor DocOps Development Helper
REM This script automates the setup and launch of the documentation site

echo ========================================
echo Accor DocOps - Development Setup
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo [1/4] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
    echo.
) else (
    echo [1/4] Virtual environment already exists.
    echo.
)

REM Activate virtual environment
echo [2/4] Activating virtual environment...
call .venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated!
echo.

REM Check if packages are installed
echo [3/4] Checking dependencies...
pip show mkdocs >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
) else (
    echo Dependencies are up to date!
)
echo.

REM Optional: Run quality checks (skip if tools not installed)
echo [4/5] Running documentation quality checks...
echo.
echo Running markdownlint...
markdownlint-cli2 docs/**/*.md 2>nul
if errorlevel 1 (
    echo Note: markdownlint not found, skipping...
)
echo.
echo Running Vale style checker...
vale docs/ 2>nul
if errorlevel 9009 (
    echo Note: Vale not found. See INSTALL_VALE_WINDOWS.md for installation instructions.
    echo Skipping Vale checks...
) else if errorlevel 1 (
    echo Vale checks completed with warnings.
)
echo.
echo Quality checks complete!
echo.

REM Start MkDocs development server
echo [5/5] Starting MkDocs development server...
echo.
echo ========================================
echo Server starting at http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo ========================================
echo.
mkdocs serve

pause
