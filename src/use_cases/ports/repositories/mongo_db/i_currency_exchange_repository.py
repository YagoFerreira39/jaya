from abc import ABC, abstractmethod

from src.domain.models.currency_exchange_model import CurrencyExchangeModel


class ICurrencyExchangeRepository(ABC):
    @classmethod
    @abstractmethod
    async def register_currency_exchange(
        cls, model: CurrencyExchangeModel
    ) -> CurrencyExchangeModel:
        pass
