from witch_doctor import WitchDoctor, InjectionType

from src.adapters.extensions.currency_exchange.currency_exchange_extension import (
    CurrencyExchangeExtension,
)
from src.adapters.extensions.currency_exchange.get_currency_exchanges_by_user_id_extension import (
    GetCurrencyExchangesByUserIdExtension,
)
from src.adapters.extensions.currency_exchange.register_currency_exchange_extension import (
    RegisterCurrencyExchangeExtension,
)
from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)
from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)
from src.adapters.repositories.mongo_db.currency_exchange_repository import (
    CurrencyExchangeRepository,
)
from src.externals.infrastructures.http_session.http_session_infrastructure import (
    HttpSessionInfrastructure,
)
from src.externals.infrastructures.mongo_db.mongo_db_collection import MongoDbCollection
from src.externals.infrastructures.mongo_db.mongo_db_infrastructure import (
    MongoDbInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
    IIocContainerConfigInfrastructure,
)
from src.externals.services.exchange_rates_service import ExchangeRatesService
from src.externals.services.ports.i_http_session_infrastructure import (
    IHttpSessionInfrastructure,
)
from src.use_cases.currency_exchange.get_currency_exchanges_by_user_id_use_case import (
    GetCurrencyExchangesByUserIdUseCase,
)
from src.use_cases.currency_exchange.register_currency_exchange_use_case import (
    RegisterCurrencyExchangeUseCase,
)
from src.use_cases.ports.extensions.currency_exchange.i_currency_exchange_extension import (
    ICurrencyExchangeExtension,
)
from src.use_cases.ports.extensions.currency_exchange.i_get_currency_exchanges_by_user_id_extension import (
    IGetCurrencyExchangesByUserIdExtension,
)
from src.use_cases.ports.extensions.currency_exchange.i_register_currency_exchange_extension import (
    IRegisterCurrencyExchangeExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_currency_exchange_repository import (
    ICurrencyExchangeRepository,
)
from src.use_cases.ports.services.i_exchange_rates_service import IExchangeRatesService
from src.use_cases.ports.use_cases.currency_exchange.i_get_currency_exchanges_by_user_id_use_case import (
    IGetCurrencyExchangesByUserIdUseCase,
)
from src.use_cases.ports.use_cases.currency_exchange.i_register_currency_exchange_use_case import (
    IRegisterCurrencyExchangeUseCase,
)


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")
        use_cases_container(
            IRegisterCurrencyExchangeUseCase,
            RegisterCurrencyExchangeUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IGetCurrencyExchangesByUserIdUseCase,
            GetCurrencyExchangesByUserIdUseCase,
            InjectionType.SINGLETON,
        )

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container("infrastructures")
        infrastructures_container(
            IMongoDbCollection, MongoDbCollection, InjectionType.SINGLETON
        )
        infrastructures_container(
            IMongoDbInfrastructure, MongoDbInfrastructure, InjectionType.SINGLETON
        )

        infrastructures_container(
            IHttpSessionInfrastructure,
            HttpSessionInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        repositories_container(
            ICurrencyExchangeRepository,
            CurrencyExchangeRepository,
            InjectionType.SINGLETON,
        )

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        extensions_container(
            IRegisterCurrencyExchangeExtension,
            RegisterCurrencyExchangeExtension,
            InjectionType.SINGLETON,
        )
        extensions_container(
            IGetCurrencyExchangesByUserIdExtension,
            GetCurrencyExchangesByUserIdExtension,
            InjectionType.SINGLETON,
        )
        extensions_container(
            ICurrencyExchangeExtension,
            CurrencyExchangeExtension,
            InjectionType.SINGLETON,
        )

        return extensions_container

    @classmethod
    def __create_services_container(cls):
        services_container = WitchDoctor.container("services")

        services_container(
            IExchangeRatesService, ExchangeRatesService, InjectionType.SINGLETON
        )

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_repositories_container()
        cls.__create_extensions_container()
        cls.__create_services_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container("use_cases")
        WitchDoctor.load_container("infrastructures")
        WitchDoctor.load_container("repositories")
        WitchDoctor.load_container("extensions")
        WitchDoctor.load_container("services")

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
