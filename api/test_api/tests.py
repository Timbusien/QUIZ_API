from fastapi import APIRouter
from database.testservice import get_questions_my_db, add_questions
from database.userservice import set_answer_db

test_router = APIRouter(prefix='/test', tags=['My Tests'])


@test_router.get('/get-questions')
async def get_questions():
    # Получаем 20 вопросво из базы данных
    questions_list = get_questions_my_db()
    if questions_list:
        return {'timer': 12, 'questions': questions_list}
    else:
        return 'Здесь ничего нет'


# Проверка ответов каждого пользователя
@test_router.post('/check-answers')
async def check_answer(user_id: int, question_id: int, user_answer: int):
    result = set_answer_db(user_id, question_id, user_answer)

    if result:
        return {'status', result}
    else:
        return 'Нет ответов'


# Добавляем вопросы
@test_router.post('/add-questions')
async def add_question(question_text: str, lvl: str, type1: str, type2: str, type3: str, type4: str, correct_answer: int):
    question_result = add_questions(question_text, lvl, correct_answer, type1, type2, type3, type4)
    if question_result:
        return {'status': 'Success', 'message': question_result}
    else:
        return 'Невозможно добавить вопрос'




