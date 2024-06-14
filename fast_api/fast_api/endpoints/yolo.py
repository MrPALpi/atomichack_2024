from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def registration_worker():
    return 'Hello world'
