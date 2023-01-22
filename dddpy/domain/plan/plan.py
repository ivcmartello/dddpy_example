class Plan:
    """Plan represents your collection of plans as an entity."""

    def __init__(
        self,
        id: int,
        description: str,
        minutes_franchise: int,
        percentage_increase: float
    ):
        self.id: int = id
        self.description = description
        self.minutes_franchise = minutes_franchise
        self.percentage_increase = percentage_increase
    
    def __eq__(self, o: object) -> bool:
        return isinstance(o, Plan) and self.id == o.id
