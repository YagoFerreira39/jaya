from fastapi import APIRouter
from starlette.routing import Router

from src.adapters.controllers.currency_exchange_controller import (
    CurrencyExchangeController,
)
from src.use_cases.data_types.responses.currency_exchange.get_currency_exchanges_by_user_id_response import (
    GetCurrencyExchangesByUserIdResponse,
)
from src.use_cases.data_types.responses.currency_exchange.register_currency_exchange_response import (
    RegisterCurrencyExchangeResponse,
)
from src.use_cases.data_types.router_requests.currency_exchange.register_currency_exchange_router_request import (
    RegisterCurrencyExchangeRouterRequest,
)


# pylint: disable=W0613


class CurrencyExchangeRouter(Router):
    __currency_exchange_router = APIRouter(prefix="/{user_id}/currency-exchange")

    @staticmethod
    def get_router() -> APIRouter:
        return CurrencyExchangeRouter.__currency_exchange_router

    @staticmethod
    @__currency_exchange_router.post(
        path="/",
        tags=["Currency Exchange"],
        response_model_exclude_none=True,
        response_model=RegisterCurrencyExchangeResponse,
    )
    async def register_currency_exchange(
        user_id: str,
        request: RegisterCurrencyExchangeRouterRequest,
    ) -> RegisterCurrencyExchangeResponse:
        response = await CurrencyExchangeController.register_currency_exchange(
            router_request=request, user_id=user_id
        )

        return response

    @staticmethod
    @__currency_exchange_router.get(
        path="/",
        tags=["Currency Exchange"],
        response_model_exclude_none=True,
        response_model=GetCurrencyExchangesByUserIdResponse,
    )
    async def get_currency_exchanges_by_user_id(
        user_id: str,
    ) -> GetCurrencyExchangesByUserIdResponse:
        response = await CurrencyExchangeController.get_currency_exchanges_by_user_id(
            user_id=user_id
        )

        return response
