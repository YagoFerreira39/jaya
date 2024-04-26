from typing import List

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.get_currency_exchanges_by_user_id_request import (
    GetCurrencyExchangesByUserIdRequest,
)
from src.use_cases.data_types.responses.currency_exchange.get_currency_exchanges_by_user_id_response import (
    GetCurrencyExchangesByUserIdResponse,
    GetCurrencyExchangesByUserIdResponsePayload,
)
from src.use_cases.ports.extensions.currency_exchange.i_get_currency_exchanges_by_user_id_extension import (
    IGetCurrencyExchangesByUserIdExtension,
)


class GetCurrencyExchangesByUserIdExtension(IGetCurrencyExchangesByUserIdExtension):
    @staticmethod
    def from_router_request_to_request(
        user_id: str,
    ) -> GetCurrencyExchangesByUserIdRequest:
        try:
            request = GetCurrencyExchangesByUserIdRequest(
                user_id=user_id,
            )

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_list_to_dto_list(
        model_list: List[CurrencyExchangeModel],
    ) -> List[CurrencyExchangeDto]:
        try:
            dto_list = [
                CurrencyExchangeDto(
                    id=str(model.id),
                    user_id=model.user_id,
                    base_currency=model.base_currency,
                    dest_currency=model.dest_currency,
                    origin_amount=model.origin_amount,
                    converted_amount=model.converted_amount,
                    exchange_rate=model.exchange_rate,
                    transaction_time=model.transaction_time,
                )
                for model in model_list
            ]

            return dto_list

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_list_to_response(
        dto_list: List[CurrencyExchangeDto],
    ) -> GetCurrencyExchangesByUserIdResponse:
        try:
            payload = [
                GetCurrencyExchangesByUserIdResponsePayload(
                    id=dto.id,
                    base_currency=dto.base_currency,
                    dest_currency=dto.dest_currency,
                    origin_amount=dto.origin_amount,
                    converted_amount=dto.converted_amount,
                    exchange_rate=dto.exchange_rate,
                    transaction_time=str(dto.transaction_time),
                )
                for dto in dto_list
            ]

            response = GetCurrencyExchangesByUserIdResponse(
                payload=payload, status=True
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
