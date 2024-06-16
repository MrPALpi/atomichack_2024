from sqlalchemy import String, Boolean, Integer, LargeBinary
from sqlalchemy.schema import Column

from fast_api.database import Base

class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    owner_id = Column(Integer(), nullable=False)
    type = Column(String(31), nullable=False)
    is_processed = Column(Boolean(), nullable=False, default=False)
    data = Column(LargeBinary)
