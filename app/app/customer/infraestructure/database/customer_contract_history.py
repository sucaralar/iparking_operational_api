import uuid

from sqlalchemy import Column, Boolean, String, DateTime, func, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.infraestructure.database.connection import Base


class CustomerContractHistory(Base):
    __tablename__ = "custormer_contract_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"))
    parking_lot_id = Column(ARRAY(UUID(as_uuid=True)))
    contract_date = Column(DateTime)
    phone_number = Column(String(15), unique=True)

    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))

    user = relationship("User")
