from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.schema import Column

from fast_api.database import Base
from fast_api.database.entities.user import User

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer(), primary_key=True)
    user_id= Column(Integer(), ForeignKey(User.id), nullable=False)
