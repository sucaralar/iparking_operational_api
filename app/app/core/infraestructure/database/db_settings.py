import os
from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    db_user: str
    db_password: str
    db_host: str
    db_name: str
    db_port: int = 5432


class GlobalBaseSettings(DatabaseSettings):
    ...


class DevelopmentSettings(GlobalBaseSettings):
    db_user: str = os.getenv("DB_USER")
    db_name: str = os.getenv("DB_NAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")


environment_settings = {
    "production": DevelopmentSettings(),
    "development": DevelopmentSettings(),
}