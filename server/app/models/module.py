from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db.base import Base

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    difficulty_level = Column(String)  # beginner, intermediate, advanced
    estimated_duration = Column(Integer)  # in minutes
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    lessons = relationship("Lesson", back_populates="module", cascade="all, delete-orphan")