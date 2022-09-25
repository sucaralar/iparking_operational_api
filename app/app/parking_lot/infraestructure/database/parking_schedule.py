import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, ForeignKey, ARRAY, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.infraestructure.database.connection import Base


class ParkingSchedule(Base):
    __tablename__ = "parking_schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    days = Column(ARRAY(String))
    start_time = Column(Time)
    end_date = Column(Time)
    is_24_hours = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    parking_lot = relationship("ParkingLot")
