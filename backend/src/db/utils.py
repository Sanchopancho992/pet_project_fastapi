"""
This module provides utility functions for database operations.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from ..pet_project.settings import settings


def get_mongodb_client() -> AsyncIOMotorClient:
    """
    Creates and returns a MongoDB database connection using the settings.

    Returns:
        AsyncIOMotorClient: The MongoDB client instance.
    """
    return AsyncIOMotorClient(settings.MONGO_DB_URL)
