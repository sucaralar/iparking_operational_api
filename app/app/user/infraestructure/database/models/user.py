import uuid

from sqlalchemy import Column, Boolean, String, UniqueConstraint, Text, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.infraestructure.database.connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(200))
    password = Column(Text)
    name = Column(String(30))
    last_name = Column(String(30))
    second_last_name = Column(String(30))
    is_active = Column(Boolean, default=True)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    modification_date = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.current_timestamp())
    creation_user = Column(UUID(as_uuid=True))
    modification_user = Column(UUID(as_uuid=True))
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"))

    role = relationship("Role")

    employee = relationship("Employee", back_populates='user')
    client = relationship("Client", back_populates='user')

    UniqueConstraint('email', 'user_type', name='unique_user')
