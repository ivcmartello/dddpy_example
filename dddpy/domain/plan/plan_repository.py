from abc import ABC, abstractmethod
from typing import Optional

from dddpy.domain.plan import Plan


class PlanRepository(ABC):
    """PlanRepository defines a repository interface for Plan entity."""

    @abstractmethod
    def find_by_description(self, description: Optional[str] = None) -> Optional[Plan]:
        raise NotImplementedError
