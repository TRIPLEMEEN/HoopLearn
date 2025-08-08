from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.security import get_current_active_user
from app.db.base import get_db
from app.models.user import User
from app.schemas.user import User as UserSchema, UserUpdate, ResetPassword, EmailSchema
from app.core.security import get_password_hash, create_access_token
from app.core.config import settings
import secrets
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/me", response_model=UserSchema)
async def read_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.put("/me", response_model=UserSchema)
async def update_user_me(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    user_data = user_update.dict(exclude_unset=True)
    
    if "password" in user_data:
        user_data["hashed_password"] = get_password_hash(user_data.pop("password"))
    
    for field, value in user_data.items():
        setattr(current_user, field, value)
    
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.post("/forgot-password")
async def forgot_password(
    email_data: EmailSchema,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == email_data.email).first()
    if user:
        # Generate reset token (valid for 1 hour)
        reset_token = secrets.token_urlsafe(32)
        reset_token_expires = datetime.utcnow() + timedelta(hours=1)
        
        user.reset_password_token = reset_token
        user.reset_password_expires = reset_token_expires
        db.commit()
        
        # In a real app, send email with reset link
        reset_link = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"
        print(f"Password reset link: {reset_link}")  # Replace with email sending
        
    # Always return success to prevent email enumeration
    return {"message": "If your email is registered, you'll receive a password reset link"}

@router.post("/reset-password")
async def reset_password(
    reset_data: ResetPassword,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.reset_password_token == reset_data.token,
        User.reset_password_expires > datetime.utcnow()
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired token"
        )
    
    user.hashed_password = get_password_hash(reset_data.new_password)
    user.reset_password_token = None
    user.reset_password_expires = None
    db.commit()
    
    return {"message": "Password updated successfully"}

@router.get("/verify-email/{token}")
async def verify_email(
    token: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.verification_token == token).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid verification token"
        )
    
    user.is_verified = True
    user.verification_token = None
    db.commit()
    
    return {"message": "Email verified successfully"}
