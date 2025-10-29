import jwt
from pydantic import ValidationError

from quizy_shared.schemas.auth import JWTPayload

ALGORITHM = "HS256"


def decode_auth_jwt_token(
    token: str,
    secret_key: str,
) -> JWTPayload:
    try:
        payload = jwt.decode(
            token, secret_key, algorithms=[ALGORITHM], leeway=60
        )
        payload.setdefault("token_type", "access")
        payload.setdefault("jti", "")

        return JWTPayload(**payload)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ValidationError):
        raise ValidationError("Invalid token")
