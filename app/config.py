from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    WEBHOOK_URL: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
