from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    SECRET_KEY: str

    class Config:
        env_prefix = "AUTH_"

