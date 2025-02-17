from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, async_sessionmaker
from sqlalchemy import select

from models import Base, User
from config import Config

# Подключение к БД через asyncpg и SQLAlchemy.
engine = create_async_engine(Config.DATABASE_URL)
AsyncSessionMaker = async_sessionmaker(engine)

async def get_users():
    async with AsyncSessionMaker() as session:
        users = await session.execute(select(User))
        return users.scalars()

async def get_users_str():
    users = await get_users()
    user_list = [user.__dict__ for user in users]
        
    # Удаление ненужных полей (например, _sa_instance_state).
    formatted_users = [{key: value for key, value in user.items() if not key.startswith('_')} for user in user_list]
    
    # Формирование сообщения с информацией о пользователях.
    message = "Список пользователей:\n"
    
    if formatted_users:
        for i, user in enumerate(formatted_users):
            message += f"{i+1}. ID: {user['username']}\n"
        return message
    else:
        return "Пользователи не найдены."

async def insert_user_if_not_exists(chat_id, username, full_name):
    async with AsyncSessionMaker() as session:
        existing_user = await session.execute(select(User).where(User.chat_id == chat_id))
        
        if not existing_user.scalars().first():
            # Создание нового пользователя и добавление его в сессию.
            new_user = User(chat_id=chat_id, username=username, full_name=full_name)
            
            # Добавление нового пользователя в сессию.
            session.add(new_user)
            
            # Коммит изменений (сохранение данных).
            await session.commit()

