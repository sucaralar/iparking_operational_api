import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.infraestructure.database.connection import Base


class Integer:
    pass


class OperationType(Base):
    __tablename__ = "operation_type"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(1))
    count = Column(Integer)
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    Index('idx_parking_lot_name', name, parking_lot_id)

    parking_lot = relationship("ParkingLot")
    operation = relationship("Operation", back_populates='operation_type')
