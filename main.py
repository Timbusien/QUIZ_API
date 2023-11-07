'''API - Aplication Programming Interface,
что значит программный интерфейс приложения.
В контексте API слово «приложение» относится к любому ПО
с определенной функцией. Интерфейс можно рассматривать как
сервисный контракт между двумя приложениями.'''

# Для запуска данного кода нужно использовать: uvicorn main:app --reload
# Вместо main ставим название файла .py

from fastapi import FastAPI
from api.test_api.tests import test_router

app = FastAPI(docs_url='/')
app.include_router(test_router)


# GET запрос на получение данных
@app.get('/1', tags=['Main Menu'])
async def homepage():
    return {'message': 'Hello everyone!'}


# POST запрос для внесения данных
@app.post('/products', tags=['Moe Shop'])
async def products(name: str, price: int):
    return {f'Product name: {name}, Product Price: {price}'}


# PUT запрос на изменение данных
@app.put('/products', tags=['Moe Shop'])
async def change_info(name: str, price: int):
    return {f'Product name: {name}, Product Price: {price}'}


# DELETE метод для удаления данных
@app.delete('/products', tags=['Moe Shop'])
async def delete(name: str, price: int):
    return {f'Product name: {name}, Product Price: {price}'}


# Параметры для запросов
@app.get('/e', tags=['Example'])
async def example_text(user_id: int, user_request: str):
    return {'messages': f'Даный пользователь стоит на {user_id} месте, и имеет сколько-то баллов и его результат {user_request}'}


@app.get('/2', tags=['About us'])
async def product():
    return {'message': 2}


@app.post('/e', tags=['Example'])
async def hw(user_name: str, user_number: int, level:str):
    return {f'Your name: {user_name}, Your number {user_number}, Your lvl: {level}'}


