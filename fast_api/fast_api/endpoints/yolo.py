from fastapi import APIRouter

router = APIRouter()

from pydantic import BaseModel

from fast_api.database import db_manager
from fast_api.database.entities.task import Task
from fast_api.core.dependencies import YoloSocket


class UploadData(BaseModel):
    user_id: int
    data: list

@router.post("/upload")
async def upload(socket: YoloSocket, data: UploadData):

    socket.sendall(b"Hello, world")
        # data = s.recv(1024)
    # task = Task(user_id = data.user_id)
    
    # async with db_manager.get_session() as session:
    #     session.add(task)
    #     await session.commit()
    #     return task
    
    return None
