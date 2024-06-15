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
    hashed = hashlib.md5(user.password.encode())
    async with db_manager.get_session() as session:
        q = select(User).where(
            User.name == user.login,
            User.password_hash == hashed.hexdigest()
        )
        res = await session.execute(q)
        return res.scalar()

    return None

@router.post("/register")
async def registration_user(user: LoginUser):
    hashed = hashlib.md5(user.password.encode())
    db_user = User(name=user.login, password_hash=hashed.hexdigest())

    async with db_manager.get_session() as session:
        session.add(db_user)
        await session.commit()
        return db_user

    return None
