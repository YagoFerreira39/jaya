from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.exceptions.entity_exceptions_reasons_enum import (
    EntityExceptionsReasonsEnum,
)


class MalformedAmountPatternException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.MALFORMED_AMOUNT_PATTERN_ERROR


class MalformedCurrencyPatternException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.MALFORMED_CURRENCY_PATTERN_ERROR
