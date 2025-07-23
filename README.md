# Math Function Calling Project

Пример проекта с использованием Ollama и function calling, где модель сама выбирает математические операции (сложение, вычитание, умножение, деление, суммирование).

## Структура

- `functions.py` — функции для вычислений
- `tools.py` — описание функций для модели (JSON Schema)
- `main.py` — основной скрипт запуска

## Запуск

Убедитесь, что установлен [Ollama](https://ollama.com/download) и модель [llama3.2:1b](https://ollama.com/library/llama3.2:1b).

```bash
pip install -r requirements.txt
```

```bash
python main.py
```
