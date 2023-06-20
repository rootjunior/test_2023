from fastapi import FastAPI

from routers import data_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(data_router, prefix="/v1/data", tags=["Data"])
