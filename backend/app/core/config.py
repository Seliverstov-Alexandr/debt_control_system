from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_URL: str
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )
settings = Settings()        