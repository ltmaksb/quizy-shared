from typing import Optional, Annotated

from pydantic import BaseModel, constr, ConfigDict
from datetime import datetime

class QuizBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[str, constr(max_length=36)]
    description: Optional[constr(max_length=255)]

class Quiz(QuizBase):
    id: str
    creator_id: str

    created_at: datetime

class Q(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    image: Optional[str]
    points: int
    time_for_answer: int
    hint: Optional[str]
    quiz_id: str