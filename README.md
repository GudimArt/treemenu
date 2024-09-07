# Проект на Django с PostgreSQL

## Описание
Этот проект представляет собой веб-приложение на Django, использующее базу данных PostgreSQL.

## Требования
- Docker
- Docker Compose

## Установка и запуск проекта

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL_репозитория>
   ```
2. Перейдите в папку проекта:
```.bash
cd <название_папки_проекта>
```
3. Создайте файл .env в корне проекта и добавьте следующие переменные:
```.env
DJANGO_SECRET_KEY=your_django_key
DJANGO_PORT=8000
POSTGRES_DB=main-db
POSTGRES_USER=admin
POSTGRES_PASSWORD=password1234
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```
4. Запустите проект с помощью команды:
```bash
  make app-up
```
После запуска проект будет доступен по адресу http://localhost:8000

Для остановки контейнеров выполните: make app-down
