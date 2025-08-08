from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings



app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for HoopLearn+ - AI-Powered Smart Basketball Coach",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers after app creation to avoid circular imports
from .api.endpoints.auth import router as auth_router
from .api.endpoints.test import router as test_router

# Include API routers
app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(test_router, prefix=f"{settings.API_V1_STR}/test", tags=["test"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to HoopLearn+ API",
        "documentation": "/docs",
        "version": "0.1.0"
    }

# Import and include routers here
# from .api.v1.endpoints import users, auth, modules, chatbot
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(modules.router, prefix="/api/v1/modules", tags=["modules"])
# app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["chatbot"])