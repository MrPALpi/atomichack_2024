import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .endpoints.main_pwa.router import router as main_pwa_router


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

# app.include_router(main_pwa_router, prefix="/main/pwa")
