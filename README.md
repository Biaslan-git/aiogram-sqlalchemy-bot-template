# aiogram-sqlalchemy-bot-template
Простой шаблон для создания телеграм ботов на aiogram 3.x

Для демонстрациии работы добавлен такой функционал:
- Ответ на команду `/start` и добавление нового пользователя в базу данных
- Вывод списка пользователей по команде `/users`
- Ответ тем же сообщение на все другие сообщения пользователя (эхо)

## Стэк:
- Aiogram 3
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker
- Docker Compose

## Запуск
### 1. Клонирование репозитория
Клонируйте репозиторий и зайдите в папку:
```bash
git clone https://github.com/Biaslan-git/aiogram-sqlalchemy-bot-template.git
cd aiogram-sqlalchemy-bot-template
```
### 2. Настройках переменных окружения
Переименуйте .env.example в .env.
Укажите API ключ вашего телеграм бота, а также произвольные значения для подключения к базе данных.
**Пример:**
```env
TELEGRAM_BOT_TOKEN=123456789:ABCBCBCBCBABSABCBS # Токен вашего Telegram бота от BotFather.
POSTGRES_USER=postgres # Имя пользователя базы данных
POSTGRES_PASSWORD=postgres # Пароль для пользователя базы данных
POSTGRES_DB=postgres # Имя базы данных
```
### 3. Запуск бота
Запустите Docker Compose:
```bash
sudo docker compose up --build -d
```
И выполните миграции с помощью Alembic:
```bash
sudo docker compose exec bot alembic revision --autogenerate -m 'initial'
sudo docker compose exec bot alembic upgrade head
```
### Готово
