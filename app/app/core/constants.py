import os

from app.core.infraestructure.database.db_settings import environment_settings

ENVIRONMENT = os.getenv("ENVIRONMENT")

SETTINGS = environment_settings.get(ENVIRONMENT)
