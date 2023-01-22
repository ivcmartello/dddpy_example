from abc import ABC, abstractmethod
from typing import Optional

from .price_command_model import PriceCalculateModel, PriceCalculatedModel
from .price_service import PriceService
from dddpy.domain.plan import PlanRepository
from dddpy.domain.plan.plan_exception import PlanNotFoundError


class PriceCommandUseCase(ABC):
    """PriceCommandUseCase defines a query usecase inteface related Price entity."""

    @abstractmethod
    def calculate_price_franchise(self, data: PriceCalculateModel) -> Optional[PriceCalculatedModel]:
        raise NotImplementedError


class PriceCommandUseCaseImpl(PriceCommandUseCase):
    """PriceCommandUseCaseImpl implements a query usecases related Price entity."""

    def __init__(self, plan_repository: PlanRepository, price_service: PriceService):
        self.__plan_repository: PlanRepository = plan_repository
        self.__price_service: PriceService = price_service

    def calculate_price_franchise(self, data: PriceCalculateModel) -> Optional[PriceCalculatedModel]:
        try:
            plan_entity = self.__plan_repository.find_by_description(description=data.plan_description)
            if not plan_entity:
                raise PlanNotFoundError

            return self.__price_service.calculate_price_franchise(
                price=data.to_entity(),
                plan=plan_entity,
                minutes=data.minutes,
            )
        except:
            raise
