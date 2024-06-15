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




YOLO_HOST = "atomic-hack-yolo" #os.environ.get('YOLO_HOST', ),
YOLO_PORT = 65432 #os.environ.get('YOLO_PORT', 65432),

async def get_yolo_tcp_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((YOLO_HOST, YOLO_PORT))
            yield s
        except ConnectionRefusedError:
            yield None


AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]
YoloSocket = Annotated[Union[socket.socket, None], Depends(get_yolo_tcp_socket)]
