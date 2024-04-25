from dataclasses import dataclass


@dataclass(slots=True)
class CurrencyExchangeDto:
    id: str
    user_id: str
    base_currency: str
    dest_currency: str
    origin_amount: float
    converted_amount: float
    exchange_rate: float
    transaction_time: str
