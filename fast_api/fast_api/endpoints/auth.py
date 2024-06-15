import sqlite3

import hashlib
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select, insert

from fast_api.database.entities.user import User

from fast_api.core.dependencies import AsyncSessionDep


router = APIRouter()


class LoginUser(BaseModel):
    login: str
    password: str


@router.post("/login")
async def registration_user(session: AsyncSessionDep, user: LoginUser):
    hashed = hashlib.md5(user.password.encode())
    q = select(User).where(
        User.name == user.login,
        User.password_hash == hashed.hexdigest()
    )
    res = await session.execute(q)
    return res.scalar()

@router.post("/register")
async def registration_user(session: AsyncSessionDep, user: LoginUser):
    hashed = hashlib.md5(user.password.encode())
    db_user = User(name=user.login, password_hash=hashed.hexdigest())
    session.add(db_user)
    await session.commit()
    return db_user
