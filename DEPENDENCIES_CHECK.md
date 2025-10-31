# Проверка зависимостей и инструментов

## ✅ Что установлено

### Python зависимости (requirements.txt)
- ✅ MkDocs и плагины:
  - mkdocs==1.6.1
  - mkdocs-material==9.6.22
  - mkdocs-glightbox==0.5.2
  - mkdocs-section-index==0.3.10
  - mkdocs-static-i18n==1.3.0
- ✅ Форматтеры:
  - mdformat==1.0.0
  - mdformat-gfm==1.0.0
- ✅ Утилиты:
  - PyYAML==6.0.3
  - textstat==0.7.3

### Конфигурационные файлы
- ✅ `.pre-commit-config.yaml` - конфигурация pre-commit hooks
- ✅ `.markdownlint.json` - конфигурация markdownlint
- ✅ `.vale.ini` - конфигурация Vale

### Инструменты валидации (tools/)
- ✅ `validate_tags.py` - валидация тегов
- ✅ `check_links.py` - проверка ссылок
- ✅ `docs_health_check.py` - проверка front matter
- ✅ `check_media.py` - проверка медиа файлов
- ✅ `generate_facets.py` - генерация facet страниц
- ✅ `generate_statistics.py` - генерация статистики
- ✅ `tags-allowlist.json` - список разрешенных тегов

## ⚠️ Проблемы и несоответствия

### 1. Pre-commit не в requirements.txt
**Проблема:** `pre-commit` не добавлен в `requirements.txt`, хотя используется в документации и ADR-005.

**Решение:** Добавить в requirements.txt:
```
pre-commit>=3.0.0
```

### 2. Дубликаты в .pre-commit-config.yaml
**Проблема:** В файле `.pre-commit-config.yaml` есть:
- Два блока `repos:`
- Дважды указан `mdformat` (версии 0.7.16 и 1.0.0)

**Решение:** Объединить в один блок repos и использовать одну версию mdformat (1.0.0).

### 3. Отсутствуют внешние инструменты
**Проблема:** В документации упоминаются инструменты, которых нет в requirements.txt:
- `markdownlint-cli2` - это Node.js инструмент (не Python)
- `vale` - это отдельный бинарный инструмент (не Python)

**Примечание:** Это нормально, так как они устанавливаются отдельно. Но нужно обновить документацию, чтобы указать способ установки.

### 4. Отсутствует .vale/styles
**Проблема:** `.vale.ini` ссылается на `StylesPath = .vale/styles`, но папка не существует.

**Решение:** Создать папку или обновить конфигурацию.

### 5. Не указаны зависимости для Python скриптов
**Проблема:** Скрипты в `tools/` используют стандартную библиотеку Python (Path, json, re), но это нормально - зависимости не нужны.

## 📋 Рекомендации

### Добавить в requirements.txt
```txt
pre-commit>=3.0.0
```

### Исправить .pre-commit-config.yaml
Убрать дубликаты и объединить в один блок repos.

### Обновить документацию
В FAQ и README добавить инструкции по установке:
- Node.js для markdownlint-cli2
- Vale binary установка

### Создать .vale/styles или обновить конфигурацию
Либо создать папку со стилями, либо обновить `.vale.ini`.

## 🔍 Что проверить вручную

1. **Node.js установлен?**
   ```bash
   node --version
   npm --version
   ```

2. **markdownlint-cli2 установлен?**
   ```bash
   markdownlint-cli2 --version
   # Если нет: npm install -g markdownlint-cli2
   ```

3. **Vale установлен?**
   ```bash
   vale --version
   # Если нет: см. https://vale.sh/docs/vale-cli/installation/
   ```

4. **Pre-commit установлен?**
   ```bash
   pre-commit --version
   # Если нет: pip install pre-commit
   ```

## ✅ Итоговый чеклист

- [ ] Добавить `pre-commit` в requirements.txt
- [ ] Исправить дубликаты в .pre-commit-config.yaml
- [ ] Проверить наличие Node.js и markdownlint-cli2
- [ ] Проверить наличие Vale
- [ ] Создать/обновить .vale/styles или конфигурацию
- [ ] Обновить документацию с инструкциями по установке внешних инструментов

---
**Дата проверки:** 2025-01-15

