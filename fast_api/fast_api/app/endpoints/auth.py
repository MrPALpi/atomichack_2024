import sqlite3
from fastapi import APIRouter

con = sqlite3.connect("atomic-hack.db")
cur = con.cursor()

router = APIRouter()
