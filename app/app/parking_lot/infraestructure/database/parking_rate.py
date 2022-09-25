import uuid
import enum

from sqlalchemy import Column, Boolean, String, DateTime, func, ARRAY, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class RateType(enum.Enum):
    hour = 'Per Hour'
    period = 'Per Period'


class ParkingRate(Base):
    __tablename__ = "parking_rate"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(30))
    is_preferential = Column(Boolean, default=False)
    parking_lot_id = Column(ARRAY(UUID(as_uuid=True)))
    rate_type = Column(Enum(RateType))
    total_hours = Column(Integer)
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    operation = relationship("Operation", back_populates='parking_rate')
    payment_history = relationship("PaymentHistory", back_populates='parking_rate')
