from fastapi import APIRouter

user_router = APIRouter(prefix='/user', tags=['Пользователи'])

@user_router.post('/register')
async def register_user():
    pass


@user_router.get('/leaders')
async def get_leaders():
    pass


@user_router.post('/done')
async def test_finished():
    pass


