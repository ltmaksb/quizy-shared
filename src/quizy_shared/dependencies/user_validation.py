from typing import Annotated

from fastapi import Depends

from quizy_shared.schemas.user import UserDetail
from quizy_shared.services.user_validation_service import UserValidationService

UserValidationDep = Annotated[UserDetail, Depends(UserValidationService.validate_user_data)]
