from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from dddpy.domain.price import Price, PriceRepository
from .price_dto import PriceDTO


class PriceRepositoryImpl(PriceRepository):
    """PlanRepositoryImpl implements CRUD operations related Plan entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.__session: Session = session

    def find_by_code_area(self, code_area_from: Optional[str] = None, code_area_to: Optional[str] = None) -> Optional[Price]:
        try:
            price_dto = self.__session.query(PriceDTO).filter_by(code_area_from=code_area_from, code_area_to=code_area_to).one()
            return price_dto.to_entity()
        except NoResultFound:
            return None
        except:
            raise
