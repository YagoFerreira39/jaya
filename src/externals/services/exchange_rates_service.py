from http import HTTPStatus

from aiohttp import ClientSession
from decouple import config
from witch_doctor import WitchDoctor

from src.domain.enums.currency_types_enum import CurrencyTypesEnum
from src.externals.infrastructures.http_session.exceptions.http_session_infrastructure_base_exception import (
    HttpSessionInfrastructureBaseException,
)
from src.externals.services.data_types.http_session.http_client_session_init_parameters import (
    HttpClientSessionInitParameters,
)
from src.externals.services.exceptions.service_exceptions import (
    HttpServiceException,
    ServiceUnexpectedException,
)
from src.externals.services.ports.i_http_session_infrastructure import (
    IHttpSessionInfrastructure,
)
from src.use_cases.ports.services.i_exchange_rates_service import IExchangeRatesService


class ExchangeRatesService(IExchangeRatesService):
    __http_session_infrastructure: IHttpSessionInfrastructure

    @WitchDoctor.injection
    def __init__(
        self,
        http_session_infrastructure: IHttpSessionInfrastructure,
    ):
        ExchangeRatesService.__http_session_infrastructure = http_session_infrastructure

    @classmethod
    async def get_exchange_rate(
        cls, base_currency: CurrencyTypesEnum, dest_currency: CurrencyTypesEnum
    ) -> float:
        try:
            http_session_parameters = HttpClientSessionInitParameters(
                base_url=config("EXCHANGE_RATE_SERVICE_URI"),
                headers={},
            )

            async with cls.__http_session_infrastructure.get_http_client_session(
                http_client_session_init_parameters=http_session_parameters
            ) as http_client_session:
                http_client_session: ClientSession

                api_key = config("EXCHANGE_RATES_API_KEY")

                result = await http_client_session.get(
                    url="/v1/latest",
                    params={
                        "apikey": api_key,
                        "base_currency": base_currency,
                        "currencies": dest_currency,
                    },
                )

                if result.status == HTTPStatus.OK:
                    json_result = await result.json(content_type=None)
                    response = json_result.get("data", {}).get(dest_currency)

                return response

        except HttpSessionInfrastructureBaseException as original_exception:
            raise HttpServiceException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except Exception as original_exception:
            raise ServiceUnexpectedException(
                message="Unexpected service exception",
                original_error=original_exception,
            ) from original_exception
