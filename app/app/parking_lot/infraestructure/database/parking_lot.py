import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class ParkingLot(Base):
    __tablename__ = "parking_lot"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    address = Column(String(100))
    places = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    parking_lot = relationship("ParkingSchedule", back_populates='parking_lot')
    parking_gate = relationship("ParkingGate", back_populates='parking_lot')
