from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.adapters.repositories.mongo_db.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.entities.currency_exchange_entity import CurrencyExchangeEntity
from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.externals.services.exceptions.service_base_exception import (
    ServiceBaseException,
)
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.register_currency_exchange_request import (
    RegisterCurrencyExchangeRequest,
)
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    MalformedRequestInputException,
    UnableToRegisterCurrencyExchange,
)
from src.use_cases.ports.extensions.currency_exchange.i_register_currency_exchange_extension import (
    IRegisterCurrencyExchangeExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_currency_exchange_repository import (
    ICurrencyExchangeRepository,
)
from src.use_cases.ports.services.i_exchange_rates_service import IExchangeRatesService
from src.use_cases.ports.use_cases.currency_exchange.i_register_currency_exchange_use_case import (
    IRegisterCurrencyExchangeUseCase,
)


class RegisterCurrencyExchangeUseCase(IRegisterCurrencyExchangeUseCase):
    __currency_exchange_repository: ICurrencyExchangeRepository
    __register_currency_exchange_extension: IRegisterCurrencyExchangeExtension
    __exchange_rates_service: IExchangeRatesService

    @WitchDoctor.injection
    def __init__(
        self,
        currency_exchange_repository: ICurrencyExchangeRepository,
        register_currency_exchange_extension: IRegisterCurrencyExchangeExtension,
        exchange_rates_service: IExchangeRatesService,
    ):
        RegisterCurrencyExchangeUseCase.__currency_exchange_repository = (
            currency_exchange_repository
        )
        RegisterCurrencyExchangeUseCase.__register_currency_exchange_extension = (
            register_currency_exchange_extension
        )
        RegisterCurrencyExchangeUseCase.__exchange_rates_service = (
            exchange_rates_service
        )

    @classmethod
    async def register_currency_exchange(
        cls, request: RegisterCurrencyExchangeRequest
    ) -> CurrencyExchangeDto:
        try:
            exchange_rate = await cls.__get_exchange_rate(request=request)

            entity = cls.__create_entity(request=request, exchange_rate=exchange_rate)

            model = cls.__create_model(entity=entity)

            inserted_model = await cls.__register_currency_exchange(model=model)

            dto = cls.__create_dto(model=inserted_model)

            return dto

        except UseCaseBaseException as original_exception:
            raise original_exception
        except Exception as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_exchange_rate(
        cls, request: RegisterCurrencyExchangeRequest
    ) -> float:
        try:
            exchange_rate = await cls.__exchange_rates_service.get_exchange_rate(
                base_currency=request.base_currency, dest_currency=request.dest_currency
            )

            return exchange_rate

        except ServiceBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    def __create_entity(
        cls,
        request: RegisterCurrencyExchangeRequest,
        exchange_rate: float,
    ) -> CurrencyExchangeEntity:
        try:
            entity = cls.__register_currency_exchange_extension.from_request_to_entity(
                request=request, exchange_rate=exchange_rate
            )

            return entity

        except EntityBaseException as original_exception:
            raise MalformedRequestInputException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except ExtensionBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_model(cls, entity: CurrencyExchangeEntity) -> CurrencyExchangeModel:
        try:
            model = cls.__register_currency_exchange_extension.from_entity_model(
                entity=entity
            )

            return model

        except ExtensionBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __register_currency_exchange(
        cls, model: CurrencyExchangeModel
    ) -> CurrencyExchangeModel:
        try:
            model = await cls.__currency_exchange_repository.register_currency_exchange(
                model=model
            )

            return model

        except RepositoryBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_dto(cls, model: CurrencyExchangeModel) -> CurrencyExchangeDto:
        try:
            dto = cls.__register_currency_exchange_extension.from_model_to_dto(
                model=model
            )

            return dto

        except ExtensionBaseException as original_exception:
            raise UnableToRegisterCurrencyExchange(
                message="Unable to register currency exchange.",
                original_error=original_exception.original_error,
            ) from original_exception
