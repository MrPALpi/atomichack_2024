import json

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, APIRouter, File, UploadFile, Form
from typing_extensions import Annotated

from fast_api.database import db_manager
from fast_api.database.entities.task import Task
from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import YoloSocket, AsyncSessionDep


router = APIRouter()


@router.post("/upload")
async def upload(
    session: AsyncSessionDep,
    socket: YoloSocket,
    files: List[UploadFile] = File(...),
    user_id: int = Form()
):
    task = Task(user_id = user_id)
    session.add(task)
    await session.commit()

    for file in files:
        bytes_list = await file.read()
        at = Attachment(
            name=file.filename,
            owner_name=task.__tablename__,
            owner_id=task.id,
            type=file.content_type,
            data=bytes_list
        )
        session.add(at)

    await session.commit()

    tcp_data = {
        "task_id": task.id
    }

    # Отправка task id для нейронки
    socket.sendall(json.dumps(tcp_data).encode('utf-8'))
    
    return {
        "file_size": len(files),
        "status": "success"
    }
