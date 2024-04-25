from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.register_currency_exchange_request import (
    RegisterCurrencyExchangeRequest,
)


class IRegisterCurrencyExchangeUseCase(ABC):
    @classmethod
    @abstractmethod
    async def register_currency_exchange(
        cls, request: RegisterCurrencyExchangeRequest
    ) -> CurrencyExchangeDto:
        pass
