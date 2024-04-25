from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.entities.currency_exchange_entity import CurrencyExchangeEntity
from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.use_cases.data_types.dtos.currency_exchange.currency_exchange_dto import (
    CurrencyExchangeDto,
)
from src.use_cases.data_types.requests.currency_exchange.register_currency_exchange_request import (
    RegisterCurrencyExchangeRequest,
)
from src.use_cases.data_types.responses.currency_exchange.register_currency_exchange_response import (
    RegisterCurrencyExchangeResponse,
    RegisterCurrencyExchangeResponsePayload,
)
from src.use_cases.data_types.router_requests.currency_exchange.register_currency_exchange_router_request import (
    RegisterCurrencyExchangeRouterRequest,
)
from src.use_cases.ports.extensions.currency_exchange.i_register_currency_exchange_extension import (
    IRegisterCurrencyExchangeExtension,
)


class RegisterCurrencyExchangeExtension(IRegisterCurrencyExchangeExtension):

    @staticmethod
    def from_router_request_to_request(
        router_request: RegisterCurrencyExchangeRouterRequest, user_id: str
    ) -> RegisterCurrencyExchangeRequest:
        try:
            request = RegisterCurrencyExchangeRequest(
                base_currency=router_request.base_currency,
                origin_amount=router_request.origin_amount,
                dest_currency=router_request.dest_currency,
                user_id=user_id,
            )

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_request_to_entity(
        request: RegisterCurrencyExchangeRequest,
        exchange_rate: float,
    ) -> CurrencyExchangeEntity:
        try:
            entity = CurrencyExchangeEntity(
                user_id=request.user_id,
                base_currency=request.base_currency,
                dest_currency=request.dest_currency,
                origin_amount=request.origin_amount,
                exchange_rate=exchange_rate,
            )

            return entity

        except EntityBaseException as original_exception:
            raise original_exception
        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_model(entity: CurrencyExchangeEntity) -> CurrencyExchangeModel:
        try:
            model = CurrencyExchangeModel(
                user_id=entity.user_id,
                base_currency=entity.base_currency,
                dest_currency=entity.dest_currency,
                origin_amount=entity.origin_amount,
                converted_amount=entity.converted_amount,
                exchange_rate=entity.exchange_rate,
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_to_dto(model: CurrencyExchangeModel) -> CurrencyExchangeDto:
        try:
            dto = CurrencyExchangeDto(
                id=str(model.id),
                user_id=model.user_id,
                base_currency=model.base_currency,
                dest_currency=model.dest_currency,
                origin_amount=model.origin_amount,
                converted_amount=model.converted_amount,
                exchange_rate=model.exchange_rate,
                transaction_time=model.transaction_time,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(
        dto: CurrencyExchangeDto,
    ) -> RegisterCurrencyExchangeResponse:
        try:
            payload = RegisterCurrencyExchangeResponsePayload(
                id=dto.id,
                user_id=dto.user_id,
                base_currency=dto.base_currency,
                dest_currency=dto.dest_currency,
                origin_amount=dto.origin_amount,
                converted_amount=dto.converted_amount,
                exchange_rate=dto.exchange_rate,
                transaction_time=str(dto.transaction_time),
            )

            response = RegisterCurrencyExchangeResponse(
                status=True, message="Registered transaction.", payload=payload
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
