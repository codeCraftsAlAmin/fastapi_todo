from database import Base
from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum as SQLEnum

from enum import Enum as PyEnum 

class Status(str,PyEnum):
    pending = "pending"
    processing = "processing"
    complete = "complete"

class Todos(Base):
    __tablename__ = "todos"

    id =  Column(Integer, primary_key=True, index=True)
    title =  Column(String(50), nullable=False)
    description = Column(String(60), nullable=False)
    priority = Column(SQLEnum(Status), nullable=False)
    complete =  Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)