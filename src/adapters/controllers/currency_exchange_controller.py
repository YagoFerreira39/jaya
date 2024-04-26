from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler
from src.use_cases.data_types.responses.currency_exchange.get_currency_exchanges_by_user_id_response import (
    GetCurrencyExchangesByUserIdResponse,
)
from src.use_cases.data_types.responses.currency_exchange.register_currency_exchange_response import (
    RegisterCurrencyExchangeResponse,
)
from src.use_cases.data_types.router_requests.currency_exchange.register_currency_exchange_router_request import (
    RegisterCurrencyExchangeRouterRequest,
)
from src.use_cases.ports.extensions.currency_exchange.i_get_currency_exchanges_by_user_id_extension import (
    IGetCurrencyExchangesByUserIdExtension,
)
from src.use_cases.ports.extensions.currency_exchange.i_register_currency_exchange_extension import (
    IRegisterCurrencyExchangeExtension,
)
from src.use_cases.ports.use_cases.currency_exchange.i_get_currency_exchanges_by_user_id_use_case import (
    IGetCurrencyExchangesByUserIdUseCase,
)
from src.use_cases.ports.use_cases.currency_exchange.i_register_currency_exchange_use_case import (
    IRegisterCurrencyExchangeUseCase,
)


class CurrencyExchangeController:

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def register_currency_exchange(
        cls,
        user_id: str,
        router_request: RegisterCurrencyExchangeRouterRequest,
        register_currency_exchange_use_case: IRegisterCurrencyExchangeUseCase,
        register_currency_exchange_extension: IRegisterCurrencyExchangeExtension,
    ) -> RegisterCurrencyExchangeResponse:
        request = register_currency_exchange_extension.from_router_request_to_request(
            user_id=user_id, router_request=router_request
        )

        use_case_response = (
            await register_currency_exchange_use_case.register_currency_exchange(
                request=request
            )
        )

        response = register_currency_exchange_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def get_currency_exchanges_by_user_id(
        cls,
        user_id: str,
        get_currency_exchanges_use_case: IGetCurrencyExchangesByUserIdUseCase,
        get_currency_exchanges_extension: IGetCurrencyExchangesByUserIdExtension,
    ) -> GetCurrencyExchangesByUserIdResponse:
        request = get_currency_exchanges_extension.from_router_request_to_request(
            user_id=user_id
        )

        use_case_response = (
            await get_currency_exchanges_use_case.get_currency_exchanges_by_user_id(
                request=request
            )
        )

        response = get_currency_exchanges_extension.from_dto_list_to_response(
            dto_list=use_case_response
        )

        return response
