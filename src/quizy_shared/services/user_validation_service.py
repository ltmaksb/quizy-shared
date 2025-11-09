from quizy_shared.dependencies.token import TokenDep
from quizy_shared.core.settings import AuthConfig
from quizy_shared.core.security import decode_auth_jwt_token
from functools import lru_cache

from quizy_shared.schemas.auth import JWTPayload


@lru_cache()
def _get_auth_config() -> AuthConfig:
    return AuthConfig() # noqa

class UserValidationService:
    @staticmethod
    async def validate_user_data(token: TokenDep) -> JWTPayload:
        config = _get_auth_config()
        return decode_auth_jwt_token(token=token.credentials, secret_key=config.SECRET_KEY)
