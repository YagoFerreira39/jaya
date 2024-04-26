from typing import List

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.ports.extensions.currency_exchange.i_currency_exchange_extension import (
    ICurrencyExchangeExtension,
)


class CurrencyExchangeExtension(ICurrencyExchangeExtension):

    @staticmethod
    def from_database_result_to_model(result: dict) -> CurrencyExchangeModel:
        try:
            model = CurrencyExchangeModel(
                id=result.get("_id"),
                user_id=result.get("user_id"),
                base_currency=result.get("base_currency"),
                dest_currency=result.get("dest_currency"),
                origin_amount=result.get("origin_amount"),
                converted_amount=result.get("converted_amount"),
                exchange_rate=result.get("exchange_rate"),
                transaction_time=result.get("transaction_time"),
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_database_result_to_model_list(
        result_list: dict,
    ) -> List[CurrencyExchangeModel]:
        try:
            model_list = [
                CurrencyExchangeExtension.from_database_result_to_model(result=result)
                for result in result_list
            ]

            return model_list

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
