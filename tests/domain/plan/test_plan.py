import pytest

from dddpy.domain.plan import Plan


class TestPlan:
    def test_constructor_should_create_instance(self):
        plan = Plan(
            id=1,
            description="Plan test",
            minutes_franchise=10,
            percentage_increase=.1,
        )

        assert plan.id == 1
        assert plan.description == "Plan test"
        assert plan.minutes_franchise == 10
        assert plan.percentage_increase == .1
