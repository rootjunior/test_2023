from fastapi import APIRouter, Query
from starlette.exceptions import HTTPException

from ext import RedisClient
from models import DataInModel, DataModel
from settings import settings

router = APIRouter()


@router.put("/write_data", response_model=DataModel, status_code=201)
async def write_data(
    payload: DataInModel,
) -> DataModel:
    redis = RedisClient(host=settings.redis_host, port=settings.redis_port)
    await redis.write_data(phone=payload.phone, address=payload.address)
    return await redis.check_data(phone=payload.phone)


@router.get("/check_data/", response_model=DataModel, status_code=200)
async def check_data(
    phone: str = Query(..., description="Phone number to receive data"),
) -> DataModel:
    redis = RedisClient(host=settings.redis_host, port=settings.redis_port)
    data = await redis.check_data(phone=phone)

    if data:
        return data
    raise HTTPException(400, f"Data with phone: {phone} not found")
