from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.schema import Column

from fast_api.database import Base

class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    owner_id = Column(Integer(), nullable=False)
    type = Column(String(31), nullable=False, default='image')
    data = Column(LargeBinary)
