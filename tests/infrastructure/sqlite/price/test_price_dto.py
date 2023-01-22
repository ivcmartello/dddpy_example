from dddpy.infrastructure.sqlite.price import PriceDTO


class TestPriceDTO:
    def test_to_entity_should_create_entity_instance(self):
        price_dto = PriceDTO(
            id=1,
            code_area_from="011",
            code_area_to="017",
            value_per_minute=1.9,
        )

        price = price_dto.to_entity()

        assert price.id == 1
        assert price.code_area_from == "011"
        assert price.code_area_to == "017"
        assert price.value_per_minute == 1.9
        assert not price.is_transient
