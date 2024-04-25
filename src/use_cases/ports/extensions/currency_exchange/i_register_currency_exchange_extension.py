from abc import ABC, abstractmethod

from src.domain.entities.currency_exchange_entity import CurrencyExchangeEntity
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.register_currency_exchange_request import (
    RegisterCurrencyExchangeRequest,
)
from src.use_cases.data_types.responses.currency_exchange.register_currency_exchange_response import (
    RegisterCurrencyExchangeResponse,
)
from src.use_cases.data_types.router_requests.currency_exchange.register_currency_exchange_router_request import (
    RegisterCurrencyExchangeRouterRequest,
)


class IRegisterCurrencyExchangeExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        router_request: RegisterCurrencyExchangeRouterRequest, user_id: str
    ) -> RegisterCurrencyExchangeRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_request_to_entity(
        request: RegisterCurrencyExchangeRequest,
        exchange_rate: float,
    ) -> CurrencyExchangeEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_model(entity: CurrencyExchangeEntity) -> CurrencyExchangeModel:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: CurrencyExchangeModel) -> CurrencyExchangeDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(
        dto: CurrencyExchangeDto,
    ) -> RegisterCurrencyExchangeResponse:
        pass
