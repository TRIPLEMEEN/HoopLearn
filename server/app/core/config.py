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
    
    class Config:
        case_sensitive = True

settings = Settings()
