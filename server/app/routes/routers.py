from fastapi import APIRouter, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/summary")
async def summary(request: Request):
    print("post /test/summary")
    return 200

@router.post("/keyword")
async def keyword(request: Request):
    print("post /test/keyword")
    return 200