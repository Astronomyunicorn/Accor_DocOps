@echo off
REM Accor DocOps - Formatting and Linting Scripts
REM This script provides tools for formatting and linting documentation

echo ========================================
echo Accor DocOps - Documentation Tools
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo ERROR: Virtual environment not found. Run dev.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated!
echo.

REM Check command
if "%1"=="format" goto format
if "%1"=="lint" goto lint
if "%1"=="check" goto check
if "%1"=="fix" goto fix
goto help

:format
echo [FORMAT] Formatting Markdown files...
mdformat docs/
echo Formatting complete!
goto end

:lint
echo [LINT] Running markdownlint...
markdownlint-cli2 docs/**/*.md
echo.
echo [LINT] Running Vale style checker...
vale docs/
goto end

:check
echo [CHECK] Running all checks...
echo.
echo [1/3] MkDocs build check...
mkdocs build --strict
if errorlevel 1 (
    echo ERROR: MkDocs build failed
    goto end
)
echo.
echo [2/3] Markdown linting...
markdownlint-cli2 docs/**/*.md
echo.
echo [3/3] Vale style checking...
vale docs/
goto end

:fix
echo [FIX] Auto-fixing issues...
echo.
echo [1/2] Formatting files...
mdformat docs/
echo.
echo [2/2] Running lint with auto-fix...
markdownlint-cli2 --fix docs/**/*.md
echo Auto-fix complete!
goto end

:help
echo Available commands:
echo   format  - Format all Markdown files
echo   lint    - Run linting checks
echo   check   - Run all quality checks
echo   fix     - Auto-fix formatting issues
echo.
echo Usage: tools.bat [command]
echo Example: tools.bat format

:end
pause
