"""
Main module for the FastAPI application.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from .db.utils import get_mongodb_client
from .api.views import router as api_router
from .pet_project.settings import settings
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for the FastAPI app.
    Initializes and closes the MongoDB connection.
    """
    client = get_mongodb_client()
    db = client.get_database(settings.MONGO_DB_DB)
    app.mongodb = db
    yield
    client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root() -> dict[str, str]:
    """
    Root endpoint that returns a greeting message.
    """
    return {"message": "Hello World"}
