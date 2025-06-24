#!/usr/bin/env bash
# Скрипт для установки в виртуальное окружение

python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Установка завершена. Активируйте окружение командой 'source venv/bin/activate' и запустите 'python bot.py'."
