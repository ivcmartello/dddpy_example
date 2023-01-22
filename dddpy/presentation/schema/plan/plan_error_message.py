from pydantic import BaseModel, Field

from dddpy.domain.plan import (
    PlanNotFoundError,
)


class ErrorMessagePlanNotFound(BaseModel):
    detail: str = Field(example=PlanNotFoundError.message)