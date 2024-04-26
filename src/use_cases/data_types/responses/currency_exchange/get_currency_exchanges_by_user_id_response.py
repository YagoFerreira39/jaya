from typing import List

from pydantic import BaseModel

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class GetCurrencyExchangesByUserIdResponsePayload(BaseModel):
    id: str
    base_currency: str
    dest_currency: str
    origin_amount: float
    converted_amount: float
    exchange_rate: float
    transaction_time: str


class GetCurrencyExchangesByUserIdResponse(BaseApiResponse):
    payload: List[GetCurrencyExchangesByUserIdResponsePayload] = None
