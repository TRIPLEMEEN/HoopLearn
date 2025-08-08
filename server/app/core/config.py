from pydantic import BaseSettings
from typing import Optional
from datetime import timedelta

class Settings(BaseSettings):
    PROJECT_NAME: str = "HoopLearn+ API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key-here"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    DATABASE_URL: str = "sqlite:///./hooplearn.db"
    FRONTEND_URL: str = "http://localhost:3000"  # Update with your frontend URL
    SMTP_SERVER: str = "smtp.example.com"  # Update with your SMTP server
    SMTP_PORT: int = 587
    SMTP_USER: str = "abdulkareemalameen18@gmail.com"
    SMTP_PASSWORD: str = "ade18boy"
    EMAIL_FROM: str = "noreply@hooplearn.com"
    class Config:
        case_sensitive = True

settings = Settings()
