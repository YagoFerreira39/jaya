from src.domain.enums.currency_types_enum import CurrencyTypesEnum
from src.domain.exceptions.entity_exceptions import (
    MalformedAmountPatternException,
    MalformedCurrencyPatternException,
)


class CurrencyExchangeEntity:
    def __init__(
        self,
        user_id: str,
        base_currency: CurrencyTypesEnum,
        dest_currency: CurrencyTypesEnum,
        origin_amount: float,
        exchange_rate: float,
    ):
        self.__user_id = user_id
        self.__base_currency = base_currency
        self.__dest_currency = dest_currency
        self.__origin_amount = origin_amount
        self.__exchange_rate = exchange_rate
        self.__converted_amount = None
        self.__create()

    @property
    def user_id(self) -> str:
        return self.__user_id

    @property
    def base_currency(self) -> str:
        return self.__base_currency

    @property
    def dest_currency(self) -> str:
        return self.__dest_currency

    @property
    def origin_amount(self) -> float:
        return self.__origin_amount

    @property
    def converted_amount(self) -> float:
        return self.__converted_amount

    @property
    def exchange_rate(self) -> float:
        return self.__exchange_rate

    def __create(self):
        self.__validate_origin_amount()
        self.__validate_base_and_dest_currency()
        self.__calculate_converted_amount()

    def __validate_origin_amount(self):
        if self.__origin_amount <= 0:
            raise MalformedAmountPatternException(
                message="Origin amount cannot be less or equal than zero."
            )

    def __validate_base_and_dest_currency(self):
        if self.__base_currency == self.__dest_currency:
            raise MalformedCurrencyPatternException(
                message="Base currency and dest currency must be different."
            )

    def __calculate_converted_amount(self):
        converted_amount = self.__origin_amount * self.__exchange_rate
        self.__converted_amount = converted_amount
