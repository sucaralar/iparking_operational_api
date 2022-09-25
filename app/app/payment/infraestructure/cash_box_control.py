import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class CashBoxControl(Base):
    __tablename__ = "cash_box_control"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cash_box_name = Column(String(2))
    receipt_counter = Column(Integer)
    year = Column(Integer)
    device_id = Column(Text)
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    cash_closing = relationship("CashClosing", back_populates='cash_box_control')
    payment_history = relationship("PaymentHistory", back_populates='cash_box_control')
