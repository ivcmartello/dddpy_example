from unittest.mock import MagicMock, Mock

import pytest

from dddpy.domain.plan import Plan, PlanNotFoundError
from dddpy.domain.price import Price
from dddpy.infrastructure.sqlite.price import PriceServiceImpl, PriceRepositoryImpl
from dddpy.infrastructure.sqlite.plan import PlanRepositoryImpl

from dddpy.usecase.price import PriceCommandUseCaseImpl, PriceCalculateModel


class TestBookQueryUseCase:
    def test_calculate_price_franchise_should_return_calculated_price(self):
        session = MagicMock()
        plan_repository = PlanRepositoryImpl(session)
        price_repository = PriceRepositoryImpl(session)
        price_service = PriceServiceImpl(price_repository)

        plan_repository.find_by_description = Mock(
            return_value=Plan(
                id=1,
                description="Plan test",
                minutes_franchise=60,
                percentage_increase=.1
            )
        )

        price_repository.find_by_code_area = Mock(
            return_value=Price(
                id=1,
                code_area_from="011",
                code_area_to="017",
                value_per_minute=1.7
            )
        )

        price_command_usecase = PriceCommandUseCaseImpl(plan_repository=plan_repository, price_service=price_service)
        price_model = PriceCalculateModel(code_area_from="011", code_area_to="017", minutes=80, plan_description="Plan test")

        price_calculated = price_command_usecase.calculate_price_franchise(price_model)

        assert price_calculated.value_with_franchise == "$ 37.40"
        assert price_calculated.value_without_franchise == "$ 136.00"
        

    def test_calculate_price_franchise_should_throw_plan_not_found_error(self):
        session = MagicMock()
        plan_repository = PlanRepositoryImpl(session)
        price_repository = PriceRepositoryImpl(session)
        price_service = PriceServiceImpl(price_repository)

        plan_repository.find_by_description = Mock(side_effect=PlanNotFoundError)
        price_command_usecase = PriceCommandUseCaseImpl(plan_repository=plan_repository, price_service=price_service)
        price_model = PriceCalculateModel(code_area_from="011", code_area_to="017", minutes=80, plan_description="Plan not saved")

        with pytest.raises(PlanNotFoundError):
            price_command_usecase.calculate_price_franchise(price_model)
