import pytest

from dddpy.domain.price import Price


class TestPrice:
    @pytest.mark.parametrize(
        "id,transient",
        [
            (1, False),
            (None, True)
        ],
    )
    def test_constructor_should_create_instance(self, id, transient):
        price = Price(
            code_area_from="011",
            code_area_to="016",
            value_per_minute=1.2,
            id=id
        )

        assert price.is_transient == transient
        assert price.code_area_from == "011"
        assert price.code_area_to == "016"
        assert price.value_per_minute == 1.2
