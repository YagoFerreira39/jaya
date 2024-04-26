from abc import ABC, abstractmethod
from typing import List

from src.domain.models.currency_exchange_model import CurrencyExchangeModel


class ICurrencyExchangeRepository(ABC):
    @classmethod
    @abstractmethod
    async def register_currency_exchange(
        cls, model: CurrencyExchangeModel
    ) -> CurrencyExchangeModel:
        pass

    @classmethod
    @abstractmethod
    async def get_currency_exchanges_by_user_id(
        cls, user_id: str
    ) -> List[CurrencyExchangeModel]:
        pass
