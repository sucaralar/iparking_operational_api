import uuid
from tokenize import String

from sqlalchemy import Column, DateTime, func, Integer, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class PaymentHistory(Base):
    __tablename__ = "payment_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    payment_datetime = Column(DateTime)
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    cashier_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    parking_rate_id = Column(UUID(as_uuid=True), ForeignKey("parking_rate.id"))
    total_time = Column(Float)
    cash_box_control_id = Column(UUID(as_uuid=True), ForeignKey("cash_box_control.id"))
    cash_box_name = Column(String(2))
    receipt = Column(Integer)
    year = Column(Integer)
    operation_id = Column(UUID(as_uuid=True), ForeignKey("operation.id"))
    billing_detail = Column(JSONB)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    parking_lot = relationship('ParkingLot')
    cashier = relationship('User')
    parking_rate = relationship('ParkingRate')
    cash_box_control = relationship('CashBoxControl')

    operation = relationship("Operation", back_populates='payment')

