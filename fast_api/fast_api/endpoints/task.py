from fastapi import APIRouter
from sqlalchemy import select, join
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from fast_api.database.entities.task import Task
from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import AsyncSessionDep

router = APIRouter()


@router.get("/user-task-list")
async def get_user_task_list(session: AsyncSessionDep, user_id: int):
    stmt = f"""
        SELECT task.id, COUNT(attachment.id)
        FROM task
        INNER JOIN attachment ON task.id = attachment.owner_id
        WHERE task.user_id = {user_id}
        GROUP BY task.id;
    """

    result = []

    res = await session.execute(text(stmt))

    for row in res.tuples():
        result.append({"task_id": row[0], "count_src": row[1]})

    return result


@router.get("/{item_id}/attachment")
async def get_task_by_id(session: AsyncSessionDep, item_id: int):
    stmt = f"""
            SELECT task.id as task_id, attachment.id as attachment_id
            FROM task
            INNER JOIN attachment ON task.id = attachment.owner_id
            WHERE task.id = {item_id};
        """

    result = {}

    res = await session.execute(text(stmt))

    for row in res.tuples():
        print(row)
        task_id = row[0]
        if result.get(task_id, None) is not None:
            result[task_id].append(row[1])
        else:
            result[task_id] = []
            result[task_id].append(row[1])

    return result
