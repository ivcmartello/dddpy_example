from dddpy.infrastructure.sqlite.database import SessionLocal
from dddpy.infrastructure.sqlite.price.price_dto import PriceDTO
from dddpy.infrastructure.sqlite.plan.plan_dto import PlanDTO


def perform_seed() -> None:
    """Perform seed defines a method to storage initial data."""
    session = SessionLocal()
    
    session.add_all([
        PriceDTO(id=1, code_area_from="011", code_area_to="016", value_per_minute=1.90),
        PriceDTO(id=2, code_area_from="016", code_area_to="011", value_per_minute=2.90),
        PriceDTO(id=3, code_area_from="011", code_area_to="017", value_per_minute=1.70),
        PriceDTO(id=4, code_area_from="017", code_area_to="011", value_per_minute=2.70),
        PriceDTO(id=5, code_area_from="011", code_area_to="018", value_per_minute=0.90),
        PriceDTO(id=6, code_area_from="018", code_area_to="011", value_per_minute=1.90)
    ])

    session.add_all([
        PlanDTO(id=1, description="FaleMais 30", minutes_franchise=30, percentage_increase=.1),
        PlanDTO(id=2, description="FaleMais 60", minutes_franchise=60, percentage_increase=.1),
        PlanDTO(id=3, description="FaleMais 120", minutes_franchise=120, percentage_increase=.1),
    ])

    session.commit()