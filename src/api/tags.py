from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_tags():
    return {"message": "Tags API"}
