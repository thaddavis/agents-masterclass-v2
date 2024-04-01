import time
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/completion")
def read_root():
    return {"completion": "Hey!"}