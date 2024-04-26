from abc import ABC, abstractmethod
from typing import List

from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.get_currency_exchanges_by_user_id_request import (
    GetCurrencyExchangesByUserIdRequest,
)
from src.use_cases.data_types.responses.currency_exchange.get_currency_exchanges_by_user_id_response import (
    GetCurrencyExchangesByUserIdResponse,
)


class IGetCurrencyExchangesByUserIdExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        user_id: str,
    ) -> GetCurrencyExchangesByUserIdRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_model_list_to_dto_list(
        model_list: List[CurrencyExchangeModel],
    ) -> List[CurrencyExchangeDto]:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_list_to_response(
        dto_list: List[CurrencyExchangeDto],
    ) -> GetCurrencyExchangesByUserIdResponse:
        pass
