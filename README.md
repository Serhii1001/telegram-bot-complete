# Telegram Bot (Complete Package)

Этот бот отвечает случайными фразами на каждое текстовое сообщение в любом чате. Пакет включает Dockerfile и скрипты для быстрого развертывания.

## Содержимое

- **bot.py** — основной код бота.
- **config.example.py** — пример конфига.
- **requirements.txt** — список зависимостей.
- **install.sh** — скрипт для установки в виртуальное окружение.
- **Dockerfile** — файл для сборки Docker-образа.
- **.dockerignore** — исключения для Docker.
- **.gitignore** — исключения для Git.

## Установка локально

1. Клонируйте репозиторий:
   ```bash
   git clone <URL вашего репозитория>
   cd <папка репозитория>
   ```
2. Дайте права на запуск скрипта:
   ```bash
   chmod +x install.sh
   ```
3. Запустите установку:
   ```bash
   ./install.sh
   ```
4. Создайте `config.py`:
   ```bash
   cp config.example.py config.py
   ```
   и заполните токен и фразы.
5. Запустите бота:
   ```bash
   python bot.py
   ```

## Запуск в Docker

1. Постройте образ:
   ```bash
   docker build -t telegram-bot .
   ```
2. Запустите контейнер:
   ```bash
   docker run -d --name telegram-bot telegram-bot
   ```

