from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_endpoint():
    return {"status": "success", "message": "HoopLearn+ API is running!"}