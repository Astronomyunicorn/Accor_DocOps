# Accor DocOps - Documentation Tools

Этот проект включает инструменты для форматирования и линтинга документации MkDocs.

## Установленные инструменты

### Форматтеры
- **mdformat** - Форматирование Markdown файлов
- **mdformat-gfm** - Поддержка GitHub Flavored Markdown

### Линтеры
- **markdownlint-cli2** - Проверка стиля Markdown
- **vale** - Проверка стиля и качества текста
- **textstat** - Анализ читаемости текста

## Использование

### Основные команды

```bash
# Форматирование всех Markdown файлов
tools.bat format

# Проверка стиля (линтинг)
tools.bat lint

# Полная проверка качества
tools.bat check

# Автоматическое исправление
tools.bat fix
```

### Индивидуальные команды

```bash
# Активация виртуального окружения
.venv\Scripts\activate

# Форматирование
mdformat docs/

# Markdown линтинг
markdownlint-cli2 docs/**/*.md

# Vale проверка стиля
vale docs/

# Сборка MkDocs
mkdocs build --strict
```

## Конфигурация

### markdownlint (.markdownlint.json)
- Максимальная длина строки: 120 символов
- Отступы: 2 пробела
- Разрешены дублирующиеся заголовки
- Отключены некоторые строгие правила

### Vale (.vale.ini)
- Проверка пассивного залога
- Проверка жаргона и клише
- Проверка сложных предложений
- Проверка орфографии

## Pre-commit Hooks (опционально)

Для автоматической проверки при коммитах:

```bash
pip install pre-commit
pre-commit install
```

## Стиль документации

См. файл `DOCUMENTATION_STYLE.md` для подробных правил стиля.

## Troubleshooting

### Ошибки установки
```bash
# Переустановка зависимостей
pip install -r requirements.txt --force-reinstall
```

### Проблемы с Vale
```bash
# Скачивание стилей Vale
vale sync
```

### Проблемы с markdownlint
```bash
# Проверка конфигурации
markdownlint-cli2 --config .markdownlint.json docs/
```
