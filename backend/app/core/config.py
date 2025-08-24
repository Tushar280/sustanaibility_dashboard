from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Sustainability Dashboard"
    POSTGRES_URI: str = "postgresql+psycopg2://postgres:postgres@db:5432/sustainability"
    REDIS_URL: str = "redis://redis:6379/0"
    JWT_SECRET: str = "change_me"
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 14
    PDF_BASE_URL: str = "http://backend:8000"
    EXPORTS_DIR: str = "/app/exports"

    class Config:
        env_file = ".env"

settings = Settings()
