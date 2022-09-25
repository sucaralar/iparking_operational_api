import uuid
import enum

from sqlalchemy import Column, Boolean, String, DateTime, func, ARRAY, Integer, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class GateType(enum.Enum):
    entry = 'Entry'
    exit = 'Exit'


class ParkingGate(Base):
    __tablename__ = "parking_access"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    raspberry_key = Column(String(30), unique=True)
    gate_type = Column(Enum(GateType))
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    parking_lot = relationship("ParkingLot")
