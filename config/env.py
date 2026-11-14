from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: SecretStr
    ALLOWED_HOSTS: list[str] = ['localhost', '127.0.0.1']
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: int = 5432


    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


env = EnvSettings()
