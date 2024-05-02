import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    This class is used to store the settings for the program.
    """

    APP_NAME: str = "Web Blog API"
    APP_VERSION: str = "1.0.0"
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_URL : str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()