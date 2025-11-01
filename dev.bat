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
    REM Check if critical plugins are installed
    pip show mkdocs-static-i18n >nul 2>&1
    if errorlevel 1 (
        echo Some plugins missing, installing dependencies...
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
)
echo.

REM Optional: Run quality checks (skip if tools not installed)
echo [4/5] Running documentation quality checks...
echo.

REM Markdownlint check (non-blocking)
echo Running markdownlint...
call markdownlint-cli2 docs/**/*.md >nul 2>&1
set LINT_EXIT=%ERRORLEVEL%
if %LINT_EXIT% EQU 9009 (
    echo Note: markdownlint not found, skipping...
) else if %LINT_EXIT% EQU 0 (
    echo Markdownlint passed with no errors.
) else (
    echo Markdownlint found some issues, continuing anyway...
)
set LINT_EXIT=
echo.

REM Vale check (non-blocking)
echo Running Vale style checker...
call vale docs/ >nul 2>&1
set VALE_EXIT=%ERRORLEVEL%
if %VALE_EXIT% EQU 9009 (
    echo Note: Vale not found. See INSTALL_VALE_WINDOWS.md for installation instructions.
) else if %VALE_EXIT% EQU 0 (
    echo Vale checks passed with no errors.
) else (
    echo Vale checks completed with warnings, continuing anyway...
)
set VALE_EXIT=
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
