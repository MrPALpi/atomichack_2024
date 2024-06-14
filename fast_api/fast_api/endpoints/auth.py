import sqlite3
from fastapi import APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from fast_api.database import db_manager
from fast_api.database.entities.user import User


import hashlib



router = APIRouter()

from pydantic import BaseModel


class LoginUser(BaseModel):
    login: str
    password: str


@router.post("/login")
async def registration_user(user: LoginUser):

    # dataBase_password = user.password
    # hashed = hashlib.md5(dataBase_password.encode())

    # async with db_manager.get_session() as session:
    #     q = select(User).where(
    #         User.name == user.login,
    #         User.password_hash == hashed.hexdigest()
    #     )
    #     res = await session.execute(q)
    #     return res.unique().scalars().all()
    return user


@router.get("/")
async def login_user():
    return "ТРАХАТЬ"
