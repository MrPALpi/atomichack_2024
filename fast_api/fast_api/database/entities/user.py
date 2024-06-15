from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.schema import Column
# from sqlalchemy.orm import relations

# Base = declarative_base()

from fast_api.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(120))
    is_admin = Column(Boolean(), default=False)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"
