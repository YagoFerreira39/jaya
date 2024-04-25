from abc import ABC, abstractmethod

from src.domain.enums.currency_types_enum import CurrencyTypesEnum


class IExchangeRatesService(ABC):
    @classmethod
    @abstractmethod
    async def get_exchange_rate(
        cls, base_currency: CurrencyTypesEnum, dest_currency: CurrencyTypesEnum
    ) -> float:
        pass
