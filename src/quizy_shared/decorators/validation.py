import functools
from collections.abc import Callable

from quizy_shared.schemas.user import UserDetail, UserRole

async def _validate_permission(**kwargs) -> None:
    session = kwargs.get("session")
    current_user: UserDetail = kwargs.get("current_user")

    if not current_user or current_user.role.name != UserRole.ADMIN:
        raise PermissionError("Admin privileges are required to perform this action.")

def admin_required(func) -> Callable:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Callable:
        await _validate_permission(**kwargs)
        return await func(*args, **kwargs)

    return wrapper
