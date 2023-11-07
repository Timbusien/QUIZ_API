from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, String, Boolean, Integer
from sqlalchemy.orm import relationship
from database import Base


# Создаём таблицу пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    number = Column(BigInteger, unique=True)


# Таблица для вопросов
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    lvl = Column(String, nullable=False)
    type1 = Column(String, nullable=False)
    type2 = Column(String, nullable=False)
    type3 = Column(String, nullable=True)
    type4 = Column(String, nullable=True)
    correct_answer = Column(Integer, nullable=False)


# Таблица ответов пользователей
class UserAnswer(Base):
    __tablename__ = 'answers'
    id = Column(String, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    question_id = Column(BigInteger, ForeignKey('question.id'))
    user_answer = Column(Integer, nullable=False)
    correctness = Column(Boolean, default=False)
    answer_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    question_fk = relationship(Question, lazy='subquery')


# Таблица лидеров
class Leaderboard(Base):
    __tablename__ = 'leaders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    correct_answers = Column(Integer, default=0)

    user_fk = relationship(User, lazy='subquery')




