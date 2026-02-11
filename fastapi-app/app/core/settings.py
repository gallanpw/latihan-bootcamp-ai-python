from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI with Scalar"
    VERSION: str = "0.1.0"

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()