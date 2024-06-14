import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints.auth import router as auth_router
from .endpoints.yolo import router as yolo_router


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
