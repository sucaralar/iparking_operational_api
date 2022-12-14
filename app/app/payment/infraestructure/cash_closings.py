import enum
import uuid

from sqlalchemy import Column, DateTime, func, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class CashClosingStatus(enum.Enum):
    open = 'Open'
    send = 'Send'
    close = 'Close'


class CashClosing(Base):
    __tablename__ = "cash_closing"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cashier_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    cash_box_control_id = Column(UUID(as_uuid=True), ForeignKey("cash_box_control.id"))
    shift_start_datetime = Column(DateTime)
    detail_start_shift = Column(JSONB)
    cars_inside_start_shift = Column(Integer)
    shift_end_datetime = Column(DateTime)
    detail_end_shift = Column(JSONB)
    cars_inside_end_shift = Column(Integer)
    cash_closing_detail = Column(JSONB)
    money_detail = Column(JSONB)
    who_accepts_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    cashier = relationship('User')
    parking_lot = relationship('ParkingLot')
    cash_box_control = relationship('CashBoxControl')
    who_accepts = relationship('User')

