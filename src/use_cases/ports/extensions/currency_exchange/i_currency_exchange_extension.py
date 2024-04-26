from abc import ABC, abstractmethod
from typing import List

from src.domain.models.currency_exchange_model import CurrencyExchangeModel


class ICurrencyExchangeExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> CurrencyExchangeModel:
        pass

    @staticmethod
    @abstractmethod
    def from_database_result_to_model_list(
        result_list: dict,
    ) -> List[CurrencyExchangeModel]:
        pass
