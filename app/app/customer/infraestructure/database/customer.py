import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.infraestructure.database.connection import Base


class Customer(Base):
    __tablename__ = "custormer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contract_number = Column(String(50), unique=True)
    contract_date = Column(DateTime)
    phone_number = Column(String(15), unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    user = relationship("User")
