import logging
from logging import config
from typing import Iterator

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm.session import Session

from dddpy.domain.plan import PlanRepository
from dddpy.domain.price import PriceRepository
from dddpy.domain.plan.plan_exception import PlanNotFoundError
from dddpy.infrastructure.sqlite.plan import PlanRepositoryImpl
from dddpy.infrastructure.sqlite.price import PriceRepositoryImpl, PriceServiceImpl

from dddpy.presentation.schema.plan.plan_error_message import ErrorMessagePlanNotFound
from dddpy.usecase.price import (
    PriceCommandUseCase,
    PriceCommandUseCaseImpl,
    PriceCalculateModel,
    PriceCalculatedModel,
    PriceService,
)

from dddpy.infrastructure.sqlite.database import SessionLocal, create_tables
from dddpy.infrastructure.seed import perform_seed


config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = FastAPI()


create_tables()


perform_seed()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def price_command_usecase(session: Session = Depends(get_session)) -> PriceCommandUseCase:
    plan_repository: PlanRepository = PlanRepositoryImpl(session)
    price_repository: PriceRepository = PriceRepositoryImpl(session)
    price_service: PriceService = PriceServiceImpl(price_repository)
    return PriceCommandUseCaseImpl(plan_repository, price_service)


@app.post(
    "/calculate_prices",
    response_model=PriceCalculatedModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessagePlanNotFound,
        },
    },
)
async def calculate_prices(
    data: PriceCalculateModel,
    price_command_usecase: PriceCommandUseCase = Depends(price_command_usecase),
):
    try:
        price_calculated = price_command_usecase.calculate_price_franchise(data)
    except PlanNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return price_calculated
