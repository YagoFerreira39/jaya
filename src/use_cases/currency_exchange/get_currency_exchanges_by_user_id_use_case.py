from typing import List

from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.get_currency_exchanges_by_user_id_request import (
    GetCurrencyExchangesByUserIdRequest,
)
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToRegisterCurrencyExchange,
    UnableToRetrieveCurrencyExchange,
)
from src.use_cases.ports.extensions.currency_exchange.i_get_currency_exchanges_by_user_id_extension import (
    IGetCurrencyExchangesByUserIdExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_currency_exchange_repository import (
    ICurrencyExchangeRepository,
)
from src.use_cases.ports.use_cases.currency_exchange.i_get_currency_exchanges_by_user_id_use_case import (
    IGetCurrencyExchangesByUserIdUseCase,
)


class GetCurrencyExchangesByUserIdUseCase(IGetCurrencyExchangesByUserIdUseCase):
    __currency_exchange_repository: ICurrencyExchangeRepository
    __get_currency_exchanges_by_user_id_extension: (
        IGetCurrencyExchangesByUserIdExtension
    )

    @WitchDoctor.injection
    def __init__(
        self,
        currency_exchange_repository: ICurrencyExchangeRepository,
        get_currency_exchanges_by_user_id: IGetCurrencyExchangesByUserIdExtension,
    ):
        GetCurrencyExchangesByUserIdUseCase.__currency_exchange_repository = (
            currency_exchange_repository
        )
        GetCurrencyExchangesByUserIdUseCase.__get_currency_exchanges_by_user_id_extension = (
            get_currency_exchanges_by_user_id
        )

    @classmethod
    async def get_currency_exchanges_by_user_id(
        cls, request: GetCurrencyExchangesByUserIdRequest
    ) -> List[CurrencyExchangeDto]:
        try:
            model_list_from_database = (
                await cls.__get_user_currency_exchanges_from_database(request=request)
            )

            dto = cls.__create_dto_list(model_list=model_list_from_database)

            return dto

        except UseCaseBaseException as original_exception:
            raise original_exception
        except Exception as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_user_currency_exchanges_from_database(
        cls, request: GetCurrencyExchangesByUserIdRequest
    ) -> List[CurrencyExchangeModel]:
        try:
            model_list = await cls.__currency_exchange_repository.get_currency_exchanges_by_user_id(
                user_id=request.user_id
            )

            return model_list

        except ExtensionBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_dto_list(
        cls, model_list: List[CurrencyExchangeModel]
    ) -> List[CurrencyExchangeDto]:
        try:
            dto_list = cls.__get_currency_exchanges_by_user_id_extension.from_model_list_to_dto_list(
                model_list=model_list
            )

            return dto_list

        except ExtensionBaseException as original_exception:
            raise UnableToRetrieveCurrencyExchange(
                message="Unable to retrieve currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception
