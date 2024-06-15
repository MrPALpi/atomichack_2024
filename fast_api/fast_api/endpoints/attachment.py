import io

from fastapi import APIRouter
from sqlalchemy import select
from starlette.responses import StreamingResponse

from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import AsyncSessionDep


router = APIRouter()


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
