import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fast_api.database import db_manager
from fast_api.endpoints.auth import router as auth_router
from fast_api.endpoints.yolo import router as yolo_router
from fast_api.endpoints.task import router as task_router


stage = os.environ.get('STAGE', 'dev')


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth")
app.include_router(yolo_router, prefix="/api/yolo")
app.include_router(task_router, prefix="/api/task")

@app.on_event("startup")
async def db_startup():
    print("Open DB connecting ...")
    await db_manager.startup()


@app.on_event("shutdown")
async def db_shutdown():
    print("Close DB connecting ...")
    await db_manager.close()
