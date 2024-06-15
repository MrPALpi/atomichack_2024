from fastapi import APIRouter
from sqlalchemy import select, join
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import io
from starlette.responses import StreamingResponse

from fast_api.database.entities.task import Task
from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import AsyncSessionDep

router = APIRouter()


@router.get("/{id}")
async def get_attachment(session: AsyncSessionDep, id: int):
    q = select(Attachment).where(Attachment.id == id)
    res = await session.execute(q)
    attachment = res.scalar()

    return StreamingResponse(io.BytesIO(attachment.data), media_type=attachment.type)
