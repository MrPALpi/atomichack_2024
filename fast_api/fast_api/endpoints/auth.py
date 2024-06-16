import hashlib
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select

from fast_api.database.entities.user import User
from fast_api.core.dependencies import AsyncSessionDep


router = APIRouter()


class LoginUser(BaseModel):
    login: str
    password: str


def get_password_hash(password: str) -> str:
    """ Получить хеш по паролю-строке """
    hashed = hashlib.md5(password.encode())
    return hashed.hexdigest()


@router.post("/login")
async def registration_user(session: AsyncSessionDep, user: LoginUser):
    q = select(User).where(
        User.name == user.login,
        User.password_hash == get_password_hash(user.password)
    )
    res = await session.execute(q)
    return res.scalar()


@router.post("/register")
async def registration_user(session: AsyncSessionDep, user: LoginUser):
    db_user = User(
        name=user.login,
        password_hash=get_password_hash(user.password)
    )
    session.add(db_user)
    await session.commit()
    return db_user
