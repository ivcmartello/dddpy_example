from typing import Optional
import pytest

from dddpy.domain.plan import Plan
from dddpy.domain.price import Price, ValueWithFranchise, ValueWithoutFranchise


class TestValueWithFranchise:
    def test_constructor_should_create_instance(self, price: Price, plan: Plan) -> None:
        instance = ValueWithFranchise(price=price, plan=plan, minutes=20)

        assert instance

    @pytest.mark.parametrize(
        "price_id,value_per_minute,minutes,minutes_franchise,value_with_franchise",
        [
            (1, 1.9, 20, 30, .0),
            (1, 1.7, 80, 60, 37.4),
            (1, 1.9, 200, 120, 167.2),
            (None, .0, 100, 30, None),
        ],
    )
    def test_instance_should_have_value(self,
        price_id: Optional[int],
        value_per_minute: float,
        minutes: int,
        minutes_franchise: int,
        value_with_franchise: Optional[float],
    ) -> None:
        price = Price(
            id=price_id,
            code_area_from="000",
            code_area_to="001",
            value_per_minute=value_per_minute
        )
        plan = Plan(id=1, 
            description="Plan test",
            minutes_franchise=minutes_franchise,
            percentage_increase=.1
        )

        instance = ValueWithFranchise(price=price, plan=plan, minutes=minutes)

        assert instance.value == value_with_franchise


class TestValueWithOutFranchise:
    def test_constructor_should_create_instance(self, price: Price, plan: Plan) -> None:
        instance = ValueWithoutFranchise(price=price, minutes=20)

        assert instance

    @pytest.mark.parametrize(
        "price_id,value_per_minute,minutes,value_without_franchise",
        [
            (1, 1.9, 20, 38.0),
            (1, 1.7, 80, 136.0),
            (1, 1.9, 200, 380.0),
            (None, .0, 100, None),
        ],
    )
    def test_instance_should_have_value(self, 
        price_id: Optional[int],
        value_per_minute: float,
        minutes: int,
        value_without_franchise: Optional[float]
    ) -> None:
        price = Price(
            id=price_id,
            code_area_from="000",
            code_area_to="001",
            value_per_minute=value_per_minute
        )

        instance = ValueWithoutFranchise(price=price, minutes=minutes)

        assert instance.value == value_without_franchise
