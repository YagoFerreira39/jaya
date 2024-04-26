from dataclasses import dataclass


@dataclass(slots=True)
class GetCurrencyExchangesByUserIdRequest:
    user_id: str
