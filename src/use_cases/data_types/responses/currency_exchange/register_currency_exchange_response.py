from pydantic import BaseModel

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class RegisterCurrencyExchangeResponsePayload(BaseModel):
    id: str
    user_id: str
    base_currency: str
    dest_currency: str
    origin_amount: float
    converted_amount: float
    exchange_rate: float
    transaction_time: str


class RegisterCurrencyExchangeResponse(BaseApiResponse):
    payload: RegisterCurrencyExchangeResponsePayload = None
