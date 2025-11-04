import os
import subprocess
import shutil
from pathlib import Path

def find_pandoc():
    """Находит pandoc в системе"""
    # Проверяем стандартный путь
    pandoc_path = shutil.which('pandoc')
    if pandoc_path:
        return pandoc_path
    
    # Проверяем через npx (если установлен через npm)
    npx_path = shutil.which('npx')
    if npx_path:
        try:
            result = subprocess.run(
                ['npx', '--yes', 'pandoc', '--version'],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                return ['npx', '--yes', 'pandoc']
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    
    return None

def convert_md_to_adoc(md_file, adoc_file, pandoc_cmd):
    """Конвертирует один Markdown файл в AsciiDoc"""
    try:
        cmd = pandoc_cmd if isinstance(pandoc_cmd, list) else [pandoc_cmd]
        cmd.extend([str(md_file), '-t', 'asciidoc', '-o', str(adoc_file)])
        
        subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"[OK] Converted: {md_file.name} -> {adoc_file.name}")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout if e.stdout else "Unknown error"
        print(f"[ERROR] Error converting {md_file.name}: {error_msg}")
        return False
    except FileNotFoundError:
        print("[ERROR] Pandoc not found. Install it first: https://pandoc.org/installing.html")
        return False

def batch_convert(source_dir, target_dir, pandoc_cmd):
    """Массовая конвертация всех .md файлов"""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Проверяем существование исходной директории
    if not source_path.exists():
        print(f"[ERROR] Source directory not found: {source_path}")
        print(f"  Please check if the path is correct.")
        return False
    
    if not source_path.is_dir():
        print(f"[ERROR] Source path is not a directory: {source_path}")
        return False
    
    # Создай целевую папку если её нет
    target_path.mkdir(parents=True, exist_ok=True)
    
    converted = 0
    failed = 0
    skipped = 0
    
    # Ищи все .md файлы
    md_files = list(source_path.rglob('*.md'))
    
    if not md_files:
        print(f"[ERROR] No .md files found in {source_path}")
        return False
    
    print(f"Found {len(md_files)} Markdown files to convert...\n")
    
    for md_file in md_files:
        # Пропусти README и другие специальные файлы если нужно
        if md_file.name in ['README.md', 'CONTRIBUTING.md', 'TOOLS_README.md']:
            skipped += 1
            print(f"[SKIP] Skipped: {md_file.name}")
            continue
        
        # Сохрани структуру папок
        relative_path = md_file.relative_to(source_path)
        target_file = target_path / relative_path.with_suffix('.adoc')
        
        # Создай промежуточные папки
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        if convert_md_to_adoc(md_file, target_file, pandoc_cmd):
            converted += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"[OK] Converted: {converted} files")
    print(f"[ERROR] Failed: {failed} files")
    print(f"[SKIP] Skipped: {skipped} files")
    print(f"{'='*50}")
    return True

if __name__ == '__main__':
    # Конвертируй документы из docs/en в content/modules
    print("="*50)
    print("Markdown to AsciiDoc Converter")
    print("="*50)
    print()
    
    # Проверяем наличие pandoc
    print("Checking for pandoc...")
    pandoc_cmd = find_pandoc()
    
    if not pandoc_cmd:
        print("[ERROR] Pandoc not found!")
        print("\nPlease install pandoc using one of these methods:")
        print("  1. Download from: https://pandoc.org/installing.html")
        print("  2. Install via Chocolatey: choco install pandoc")
        print("  3. Install via npm: npm install -g pandoc (if available)")
        print("\nOr run this script after installing pandoc.")
        exit(1)
    
    if isinstance(pandoc_cmd, list):
        print(f"[OK] Found pandoc via: {' '.join(pandoc_cmd)}")
    else:
        print(f"[OK] Found pandoc at: {pandoc_cmd}")
    
    print()
    print("Starting conversion...\n")
    
    success = batch_convert('./docs/en', './content/modules/ROOT/pages', pandoc_cmd)
    
    if success:
        print("\n[OK] Conversion process completed!")
    else:
        print("\n[ERROR] Conversion process failed!")
        exit(1)

