from abc import ABC, abstractmethod
from typing import List

from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.get_currency_exchanges_by_user_id_request import (
    GetCurrencyExchangesByUserIdRequest,
)


class IGetCurrencyExchangesByUserIdUseCase(ABC):
    @classmethod
    @abstractmethod
    async def get_currency_exchanges_by_user_id(
        cls, request: GetCurrencyExchangesByUserIdRequest
    ) -> List[CurrencyExchangeDto]:
        pass
