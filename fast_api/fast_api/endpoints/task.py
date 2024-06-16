from fastapi import APIRouter
from sqlalchemy import select, join
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from fast_api.database.entities.task import Task
from fast_api.database.entities.attachment import Attachment
from fast_api.core.dependencies import AsyncSessionDep
from fast_api.database.entities.defect import Defect

router = APIRouter()


@router.get("/user-task-list")
async def get_user_task_list(session: AsyncSessionDep, user_id: int):
    stmt = f"""
        SELECT
            task.id,
            task.created_date,
            COUNT(attachment.id),
            (SELECT Count(*) FROM attachment WHERE is_processed = False AND owner_id = task.id) as NotProcessedCount,
            (SELECT Count(*) FROM attachment WHERE is_processed = True AND owner_id = task.id) as ProcessedCount
        FROM task
        INNER JOIN attachment ON task.id = attachment.owner_id
        WHERE task.user_id = {user_id}
        GROUP BY task.id
        ORDER BY task.created_date DESC;
    """

    result = []

    res = await session.execute(text(stmt))

    for row in res.tuples():
        status = "success" if int(row[3]) == 0 else "process"
        result.append({"task_id": row[0], "count_src": row[2], "created_date": row[1], "status": status})

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


@router.get("/{task_id}")
async def get_task(session: AsyncSessionDep, task_id: int):
    stmt = f"""
            SELECT attachment.id, attachment.is_processed, defect.name
            FROM task
            INNER JOIN attachment ON task.id = attachment.owner_id
            LEFT JOIN defect ON attachment.id = defect.attachment_id
            WHERE task.id = {task_id};
        """

    images = dict()

    res = await session.execute(text(stmt))

    for row in res.tuples():
        if images.get(row[0]) is None:
            images[row[0]] = {"id": row[0], "is_processed": row[1], "defects": [row[2], ]}
        else:
            images[row[0]]["defects"].append(row[2])

    return {"images": images}
