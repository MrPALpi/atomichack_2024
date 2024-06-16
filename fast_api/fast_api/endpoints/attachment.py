import io

from fastapi import APIRouter
from sqlalchemy import select
from starlette.responses import StreamingResponse

from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import AsyncSessionDep

from sqlalchemy import join
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from fast_api.database.entities.task import Task
from fast_api.database.entities.defect import Defect


router = APIRouter()


@router.get("/")
async def get_attachment_for_yolo(session: AsyncSessionDep):
    stmt = f"""
            SELECT attachment.id
            FROM attachment
            WHERE is_processed = False;
        """

    res = await session.execute(text(stmt))

    result_data = []

    for row in res.tuples():
        result_data.append(row[0])

    return result_data


@router.get("/{attachment_id}")
async def get_attachment(session: AsyncSessionDep, attachment_id: int):
    q = select(Attachment).where(Attachment.id == attachment_id)
    res = await session.execute(q)
    attachment = res.scalar()

    if attachment is None:
        return None

    return StreamingResponse(
        io.BytesIO(attachment.data),
        media_type=attachment.type
    )

@router.post("/processed/{attachment_id}")
async def set_processed_attachment(session: AsyncSessionDep, attachment_id: int):
    q = select(Attachment).where(Attachment.id == attachment_id)
    res = await session.execute(q)
    attachment = res.scalar()

    if attachment is None:
        return None

    return StreamingResponse(
        io.BytesIO(attachment.data),
        media_type=attachment.type
    )
