from fastapi import APIRouter

router = APIRouter()

@router.get("/user-task-list")
async def get_user_task_list():
    return 'Hello world'

@router.get("/{item_id}")
async def get_tsak_by_id():
    return "bye bye tasl 1"
