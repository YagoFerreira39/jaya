from dataclasses import dataclass

from src.domain.enums.currency_types_enum import CurrencyTypesEnum


@dataclass(slots=True)
class RegisterCurrencyExchangeRequest:
    user_id: str
    base_currency: CurrencyTypesEnum
    dest_currency: CurrencyTypesEnum
    origin_amount: float
