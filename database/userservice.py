from .models import User, UserAnswer, Leaderboard, Question
from datetime import datetime
from database import get_database


# Регистрация
def register(name, number):
    my_db = next(get_database())

    # Валидация
    check = my_db.query(User).filter_by(number=number).first()
    if check:
        return check.id
    else:
        new_user = User(name=name, number=number, reg_date=datetime.now())
        my_db.add(new_user)
        my_db.commit()
        return new_user.id


# Запись ответов
def set_answer_db(user_id, question_id, user_answer):
    # Подключаем
    my_db = next(get_database())

    # Найти ответ
    exact_question = my_db.query(Question).filter_by(id=question_id).first()

    # Если есть вопрос
    if exact_question:
        # Сравниваем ответы
        if exact_question.correct_answer == user_answer:
            correctness = True
        # Если нет привильных ответов
        else:
            correctness = False

        # Создаём объект для базыданных
            new_answer = UserAnswer(user_id=user_id,
                                    question_id=question_id,
                                    user_answer=user_answer,
                                    correctness=correctness)
            my_db.add(new_answer)
            my_db.commit()

        return True if correctness else False
    return 'Вопрос не найден'


# Увеличиваеим баллы пользователя
def increment_user_points_db(user_id, correct_answers):
    # Создаём подключение к нашей базе данных
    my_db = next(get_database())
    check = my_db.query(Leaderboard).filter_by(user_id=user_id).first()

    if check:
        check.correct_answers += correct_answers
    else:
        new_leader_data = Leaderboard(user_id=user_id, correct_answers=correct_answers)
        my_db.add(new_leader_data)
        my_db.commit()


# Получаем место какое занял пользователь в таблице лидеров
    all_leaders = my_db.query(Leaderboard.user_id).order_by(Leaderboard.correct_answers.desc())
    return all_leaders.index(user_id) + 1





