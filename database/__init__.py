from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Мы тут указываем ссылку на нашу базу данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# Подключаемся к базе
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Создаем базу и присоединяемся к ней
SessionLocal = sessionmaker(bind=engine)
# Используем переменную Base для наследованя в таблицах
Base = declarative_base()


# Импортирование всех моделей
from database import models


# Генератор для подсоединения к базе
def get_database():
    my_database = SessionLocal()
    try:
        yield my_database
    except Exception:
        my_database.rollback()
        raise
    finally:
        my_database.close()