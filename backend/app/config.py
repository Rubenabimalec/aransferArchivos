from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # PostgreSQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    # App
    SECRET_KEY: str
    MAX_FILE_SIZE_MB: int = 100
    UPLOAD_DIR: str = "/app/uploads"
    FILE_EXPIRY_HOURS: int = 48
    ALLOWED_EXTENSIONS: str = "pdf,png,jpg,jpeg,gif,zip,txt,docx,xlsx"

    # Supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def allowed_extensions_list(self) -> List[str]:
        return [ext.strip() for ext in self.ALLOWED_EXTENSIONS.split(",")]

    @property
    def max_file_size_bytes(self) -> int:
        return self.MAX_FILE_SIZE_MB * 1024 * 1024

    class Config:
        env_file = ".env"


settings = Settings()