"""
This module provides a MongoDB client singleton that retrieves the MongoDB instance from the FastAPI app context.
"""

import importlib
from typing import cast, Any

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pymongo.results import InsertOneResult

from src.api.models import MongoDBModel


class MongoDBClient:  # pylint: disable=too-few-public-methods
    """
    A singleton client for interacting with MongoDB.
    This class ensures that only one instance of the MongoDB client is created and shared across the application.
    """

    __instance = None
    mongodb: AsyncIOMotorDatabase

    def __new__(cls) -> "MongoDBClient":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            app = get_current_app()
            cls.__instance.mongodb = app.mongodb
        return cls.__instance

    def get_collection(self, model: MongoDBModel) -> AsyncIOMotorCollection:
        """
        Retrieves the MongoDB collection for the given model.
        """
        collection_name = model.get_collection_name()
        return self.mongodb.get_collection(collection_name)

    async def insert(
        self, model: MongoDBModel, data: dict[str, Any]
    ) -> InsertOneResult:
        """
        Inserts a document into the specified model's collection.
        """
        collection = self.get_collection(model)
        return await collection.insert_one(data)

    async def get(self, model: MongoDBModel, document_id: str) -> dict[str, Any]:
        """
        Retrieves a document by its ID from the specified model's collection.
        """
        collection = self.get_collection(model)
        result = cast(dict[str, Any], await collection.find_one({"_id": document_id}))
        return result | {"id": result.pop("_id")}  # _id -> id


def get_current_app() -> FastAPI:
    """
    Retrieves the current FastAPI application instance by dynamically importing it.
    This is useful for accessing the app's MongoDB instance.
    """
    module = importlib.import_module("src.main")
    field = "app"
    return cast(FastAPI, getattr(module, field))
