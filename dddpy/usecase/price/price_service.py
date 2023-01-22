from abc import ABC, abstractmethod
from typing import Optional

from dddpy.domain.price import Price
from dddpy.domain.plan import Plan
from .price_command_model import PriceCalculatedModel


class PriceService(ABC):
    """PriceService defines a query service inteface related Price entity."""

    @abstractmethod
    def calculate_price_franchise(self, price: Price, plan: Plan,  minutes: int) -> Optional[PriceCalculatedModel]:
        raise NotImplementedError
