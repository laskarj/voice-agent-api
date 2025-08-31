from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        frozen=True,
        env_file='.env',
        extra='ignore',
        case_sensitive=True,
    )

    OPENAI_API_KEY: str
