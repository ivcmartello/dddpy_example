import pytest
from dddpy.domain.plan import Plan
from dddpy.domain.price import Price


@pytest.fixture(scope="module", name="plan")
def plan_fixture() -> Plan:
    return Plan(
        id=1, 
        description="Plan fixture", 
        minutes_franchise=30, 
        percentage_increase=.1
    )

@pytest.fixture(scope="module", name="price")
def price_fixture() -> Price:
    return Price(
        code_area_from="011",
        code_area_to="016",
        value_per_minute=1.9,
        id=1
    )