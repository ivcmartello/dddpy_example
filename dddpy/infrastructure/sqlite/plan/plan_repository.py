from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from dddpy.domain.plan import Plan, PlanRepository
from .plan_dto import PlanDTO


class PlanRepositoryImpl(PlanRepository):
    """PlanRepositoryImpl implements CRUD operations related Plan entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.__session: Session = session

    def find_by_description(self, description: Optional[str] = None) -> Optional[Plan]:
        try:
            plan_dto = self.__session.query(PlanDTO).filter_by(description=description).one()
            return plan_dto.to_entity()
        except NoResultFound:
            return None
        except:
            raise
