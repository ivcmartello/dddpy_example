from typing import Union

from sqlalchemy import Column, Integer, String, Float
from dddpy.domain.plan.plan import Plan

from dddpy.infrastructure.sqlite.database import Base


class PlanDTO(Base):
    """PlanDTO is a data transfer object associated with Plan entity."""

    __tablename__ = "plan"
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    description: Union[str, Column] = Column(String, index=True, nullable=False)
    minutes_franchise: Union[int, Column] = Column(Integer, nullable=False)
    percentage_increase: Union[float, Column] = Column(Float, nullable=False)

    def to_entity(self) -> Plan:
        return Plan(
            id=self.id,
            description=self.description,
            minutes_franchise=self.minutes_franchise,
            percentage_increase=self.percentage_increase,
        )