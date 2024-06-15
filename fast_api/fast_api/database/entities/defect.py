from sqlalchemy import String, Boolean, Integer, LargeBinary, ForeignKey
from sqlalchemy.schema import Column

from fast_api.database import Base
from fast_api.database.entities.attachment import Attachment


class Defect(Base):
    __tablename__ = "defect"

    id = Column(Integer(), primary_key=True)
    attachment_id = Column(Integer(), ForeignKey(Attachment.id), nullable=False)
    name = Column(String(255), nullable=False)
