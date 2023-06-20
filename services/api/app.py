from fastapi import FastAPI
from loguru import logger

from urls import setup_routers

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    logger.info("Setting up...")
    setup_routers(app=app)
    logger.info("Accepting connections now...")


@app.on_event("shutdown")
async def shutdown() -> None:
    logger.info("Bye now...")
    logger.info("Shutting down...")
