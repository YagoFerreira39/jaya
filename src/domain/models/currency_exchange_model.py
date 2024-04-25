from dataclasses import dataclass, field
import datetime

from bson import ObjectId


@dataclass(slots=True)
class CurrencyExchangeModel:
    user_id: str
    base_currency: str
    dest_currency: str
    origin_amount: float
    converted_amount: float
    exchange_rate: float
    id: ObjectId = field(default_factory=ObjectId)
    transaction_time: datetime = None

    def to_insert(self) -> dict:
        to_insert = {
            "user_id": self.user_id,
            "base_currency": self.base_currency,
            "dest_currency": self.dest_currency,
            "origin_amount": self.origin_amount,
            "converted_amount": self.converted_amount,
            "exchange_rate": self.exchange_rate,
            "_id": self.id,
            "transaction_time": datetime.datetime.now(tz=datetime.timezone.utc),
        }

        return to_insert
