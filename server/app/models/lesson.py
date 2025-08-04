from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db.base import Base
import enum

class LessonType(str, enum.Enum):
    THEORY = "theory"
    PRACTICE = "practice"
    QUIZ = "quiz"

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    content = Column(Text)  # Could be markdown or HTML
    lesson_type = Column(Enum(LessonType), default=LessonType.THEORY)
    order = Column(Integer)  # For sorting lessons within a module
    module_id = Column(Integer, ForeignKey("modules.id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    module = relationship("Module", back_populates="lessons")
    progress = relationship("UserProgress", back_populates="lesson")