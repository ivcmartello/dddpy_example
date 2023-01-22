from abc import ABC, abstractmethod
from typing import Optional

from dddpy.domain.price import Price


class PriceRepository(ABC):
    """PriceRepository defines a repository interface for Price entity."""

    @abstractmethod
    def find_by_code_area(self, code_area_from: Optional[str] = None, code_area_to: Optional[str] = None) -> Optional[Price]:
        raise NotImplementedError
