from typing import Optional


class Price:
    """Price represents your collection of prices as an entity."""

    def __init__(
        self,
        code_area_from: str,
        code_area_to: str,
        value_per_minute: float = .0,
        id: Optional[int] = None,
    ):
        self.code_area_from = code_area_from
        self.code_area_to = code_area_to
        self.value_per_minute = value_per_minute
        self.id = id

    @property
    def is_transient(self) -> bool:
        return self.id is None

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Price) and self.id == o.id