import enum
import uuid

from sqlalchemy import Column, Enum, DateTime, func, ForeignKey, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.infraestructure.database.connection import Base


class OperationStatus(enum.Enum):
    open = "Open"
    close = "Close"


class PaymentStatus(enum.Enum):
    pending = "Pending"
    paid = "Paid"


class Operation(Base):
    __tablename__ = "operation"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parking_lot_id = Column(UUID(as_uuid=True), ForeignKey("parking_lot.id"))
    type_operation_id = Column(UUID(as_uuid=True), ForeignKey("operation_type_id.id"))
    type_operation_name = Column(String(1))
    operation_number = Column(Integer)
    entry_parking_gate_id = Column(UUID(as_uuid=True), ForeignKey("parking_gate.id"))
    entry_datetime = Column(DateTime)
    exit_parking_gate_id = Column(UUID(as_uuid=True), ForeignKey("parking_gate.id"), nullable=True)
    exit_datetime = Column(DateTime, nullable=True)
    status = Column(Enum(OperationStatus))

    total_time = Column(Float)
    parking_rate_id = Column(UUID(as_uuid=True), ForeignKey("parking_rate.id"))
    payment_status = Column(Enum(PaymentStatus), nullable=True)
    payment_id = Column(Enum(PaymentStatus), nullable=True)
    payment_status = Column(UUID(as_uuid=True), ForeignKey("payment.id"), nullable=True)

    customer_contract_history_id = Column(UUID(as_uuid=True), ForeignKey("customer_contract_history.id"), nullable=True)

    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    parking_lot = relationship("ParkingLot")
    operation_type = relationship("OperationType")
    entry_parking_gate = relationship("ParkingGate")
    exit_parking_gate = relationship("ParkingGate")
    parking_rate = relationship("ParkingRate")
    payment = relationship("PaymentHistory")
    customer_contract_history = relationship("CustomerContractHistory")
