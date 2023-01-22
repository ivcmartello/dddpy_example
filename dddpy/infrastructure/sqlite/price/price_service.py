from typing import Optional

from dddpy.domain.price import Price, PriceRepository, ValueWithoutFranchise, ValueWithFranchise
from dddpy.domain.plan import Plan

from dddpy.usecase.price import PriceService, PriceCalculatedModel


class PriceServiceImpl(PriceService):
    """PriceCalculateServiceImpl implements operations related Price entity using SQLAlchemy."""

    def __init__(self, price_repository: PriceRepository):
        self.__price_repository: PriceRepository = price_repository

    def calculate_price_franchise(self, price: Price, plan: Plan, minutes: int) -> Optional[PriceCalculatedModel]:
        try:
            price_entity = self.__price_repository.find_by_code_area(code_area_from=price.code_area_from, code_area_to=price.code_area_to)
            if not price_entity is None:
                price = price_entity    
        except:
            raise
    
        value_with_franchise=ValueWithFranchise(price=price, plan=plan, minutes=minutes)
        value_without_franchise=ValueWithoutFranchise(price=price, minutes=minutes)

        return PriceCalculatedModel.from_entity(
            price, 
            plan_description=plan.description, 
            minutes=minutes,
            value_with_franchise=value_with_franchise,
            value_without_franchise=value_without_franchise,
        )
