import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    DB_URL: str = 'postgresql+asyncpg://user:password@host:port/dbname' # TODO: fix credentials
    BASE_SITE: str
    FRONT_SITE: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )


settings = Settings()
database_url = settings.DB_URL