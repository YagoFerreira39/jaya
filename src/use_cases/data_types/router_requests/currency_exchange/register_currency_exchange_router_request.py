from pydantic import BaseModel, StrictFloat

from src.domain.enums.currency_types_enum import CurrencyTypesEnum


class RegisterCurrencyExchangeRouterRequest(BaseModel):
    base_currency: CurrencyTypesEnum
    origin_amount: StrictFloat
    dest_currency: CurrencyTypesEnum
