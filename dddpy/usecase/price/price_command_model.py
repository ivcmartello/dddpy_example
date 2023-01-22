from pydantic import BaseModel, Field, validator

from dddpy.domain.price import Price, ValueWithoutFranchise, ValueWithFranchise


DASH = "-"
DOLAR = "$"

class PriceBaseModel(BaseModel):

    code_area_from: str = Field(max_length=3, example="011")
    code_area_to: str = Field(max_length=3, example="016")
    minutes: int = Field(gt=0, example=10)
    plan_description: str = Field(max_length=50, example="FaleMais 30")

    class Config:
        orm_mode = False


class PriceCalculateModel(PriceBaseModel):
    """PriceCalculateModel represents data structure as a calculate model."""

    class Config:
        orm_mode = False

    def to_entity(self) -> Price:
        return Price(
            code_area_from=self.code_area_from,
            code_area_to=self.code_area_to,
        )


class PriceCalculatedModel(PriceBaseModel):
    """PriceCalculatedModel represents data structure as a calculated model."""

    value_with_franchise: str = Field(example="$ 10.00")
    value_without_franchise: str = Field(example="$ 20.00")

    @validator('value_with_franchise', 'value_without_franchise')
    def value_must_contain_value_or_dash(cls, value: str) -> str:
        if "None" in value or DASH in value :
            return DASH

        if DOLAR in value:
            return value

        return DOLAR + ' %.2f' % float(value)

    class Config:
        orm_mode = False

    @staticmethod
    def from_entity(
        price: Price, 
        plan_description: str, 
        minutes: int, 
        value_with_franchise: ValueWithFranchise, 
        value_without_franchise: ValueWithoutFranchise
    ) -> "PriceCalculatedModel":
        return PriceCalculatedModel(
            code_area_from=price.code_area_from,
            code_area_to=price.code_area_to,
            minutes=minutes,
            plan_description=plan_description,
            value_with_franchise=str(value_with_franchise.value),
            value_without_franchise=str(value_without_franchise.value),
        )
