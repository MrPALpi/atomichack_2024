import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.schema import Column
from sqlalchemy.sql import func

from fast_api.database import Base
from fast_api.database.entities.user import User

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey(User.id), nullable=False)
    created_date = Column(DateTime(), default=func.now())
