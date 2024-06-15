import json

from pydantic import BaseModel
# from zipfile import ZipFile
# import aiofiles
from typing import List
from fastapi import FastAPI, APIRouter, File, UploadFile, Form
from typing_extensions import Annotated

from fast_api.database import db_manager
from fast_api.database.entities.task import Task
from fast_api.database.entities.attachment import Attachment
from fast_api.database.entities.defect import Defect
from fast_api.core.dependencies import YoloSocket, AsyncSessionDep

router = APIRouter()


async def upload_zip(file: UploadFile, db_session: AsyncSessionDep):
    async with aiofiles.open(f"./{file.filename}", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)


    zf = ZipFile(f"./{file.filename}", 'r')
    zf.extractall('./')
    zf.close()


@router.post("/upload-src")
async def upload_src(
        session: AsyncSessionDep,
        socket: YoloSocket,
        files: List[UploadFile] = File(...),
        user_id: int = Form()
):
    task = Task(user_id=user_id)
    session.add(task)
    await session.commit()

    for file in files:
        if file.content_type == "application/zip":
            # await upload_zip(file, session)
            continue

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
    yolo_error = False

    # Отправка task id для нейронки
    if socket is not None:
        socket.sendall(json.dumps(tcp_data).encode('utf-8'))
    else:
        yolo_error = True

    return {
        "file_size": len(files),
        "status": "failed" if yolo_error else "success"
    }


@router.post("/upload-result")
async def upload_result():
    Defect(attachment_id=2, name="test_deffect")
    return []
