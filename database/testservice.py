from .models import Leaderboard, Question
from database import get_database


# Функция для вывода лидеров
def get_leaders():
    my_db = next(get_database())
    leaders = my_db.query(Leaderboard.user_id).order_by(Leaderboard.correct_answers.desk())

    return leaders[:10]


# Добавление вопросов в базу
def add_questions(question_text, lvl, type1, type2, type3, type4, correct_answer):
    my_db = next(get_database())
    new_question = Question(question_text=question_text,
                            lvl=lvl,
                            type1=type1,
                            type2=type2,
                            type3=type3,
                            type4=type4,
                            correct_answer=correct_answer)
    my_db.add(new_question)
    my_db.commit()
    return 'Вопросы были успешно добвлены'


# Ввод 20 вопросов в базе данных
def get_questions_my_db():
    my_db = next(get_database())
    question = my_db.query(Question).all()

    return question[:20]



