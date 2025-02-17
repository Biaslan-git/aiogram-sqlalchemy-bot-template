from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

from sqlalchemy.ext.asyncio import AsyncSession

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer(), primary_key=True)
    chat_id = Column(Integer(), nullable=False)
    username = Column(String(50), nullable=True)
    full_name = Column(String(50), nullable=False)
    
