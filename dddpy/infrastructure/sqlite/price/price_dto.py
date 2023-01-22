from typing import Union

from sqlalchemy import Column, Integer, String, Float
from dddpy.domain.price import Price

from dddpy.infrastructure.sqlite.database import Base


class PriceDTO(Base):
    """PriceDTO is a data transfer object associated with Price entity."""

    __tablename__ = "price"
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    code_area_from: Union[str, Column] = Column(String, index=True, nullable=False)
    code_area_to: Union[str, Column] = Column(String, index=True, nullable=False)
    value_per_minute: Union[float, Column] = Column(Float, nullable=False)

    def to_entity(self) -> Price:
        return Price(
            id=self.id,
            code_area_from=self.code_area_from,
            code_area_to=self.code_area_to,
            value_per_minute=self.value_per_minute,
        )
