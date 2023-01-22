from abc import ABC
from dataclasses import dataclass
from typing import Optional

from dddpy.domain.price import Price
from dddpy.domain.plan import Plan


class BaseValue(ABC):

    value: Optional[float]

    def __init__(self, value: Optional[float]):
        object.__setattr__(self, "value", value)


@dataclass(init=False, eq=True, frozen=True)
class ValueWithoutFranchise(BaseValue):
    """ValueWithoutFranchise represents an value without plan"""

    def __init__(self, price: Price, minutes: int):
        
        value = None

        if not price.is_transient:        
            value = price.value_per_minute * minutes
        
        super().__init__(value)
       

@dataclass(init=False, eq=True, frozen=True)
class ValueWithFranchise(BaseValue):
    """ValueWithFranchise represents an value with plan"""

    def __init__(self, price: Price, plan: Plan, minutes: int):
        
        value = None

        if not price.is_transient:
            value = .0
            exceeded_minutes = minutes - plan.minutes_franchise
            if exceeded_minutes > 0:
                exceeded_value = exceeded_minutes * price.value_per_minute
                exceeded_percentage_value = exceeded_value * plan.percentage_increase
                value = exceeded_value + exceeded_percentage_value

        super().__init__(value)
