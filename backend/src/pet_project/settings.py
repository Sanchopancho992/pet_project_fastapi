"""
This module defines the settings for the FastAPI application using Pydantic's BaseSettings.
It loads environment variables from the `.env` file.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class that holds the application's configuration.
    The values are read from environment variables, with a prefix of 'app_'.
    """

    MONGO_DB_URL: str
    MONGO_DB_DB: str
    ALLOWED_ORIGINS: list[str]

    class Config:  # pylint: disable=too-few-public-methods
        """
        Configuration for the Settings class.
        Specifies the environment file and the encoding.
        """

        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"


# Create an instance of the Settings class to use throughout the app.
settings = Settings()
