from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db.base import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    lesson_id = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"))
    is_completed = Column(Boolean, default=False)
    score = Column(Float, default=0.0)  # For quizzes
    last_accessed = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="progress")
    lesson = relationship("Lesson", back_populates="progress")