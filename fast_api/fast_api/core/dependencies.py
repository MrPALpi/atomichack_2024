import os
import socket
from typing import Annotated, Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fast_api.database import db_manager


async def get_async_session() -> AsyncSession:
    """ Получениет транзакции """
    async with db_manager.get_session() as session:
        yield session


AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]
