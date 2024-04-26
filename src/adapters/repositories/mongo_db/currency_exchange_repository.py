from typing import List

from decouple import config
from witch_doctor import WitchDoctor

from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)
from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)
from src.adapters.repositories.mongo_db.exceptions.repository_exceptions import (
    FailToInsertException,
    FailToRetrieveInformationException,
)
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.externals.infrastructures.mongo_db.exceptions.mongo_db_base_infrastructure_exception import (
    MongoDbBaseInfrastructureException,
)
from src.use_cases.ports.extensions.currency_exchange.i_currency_exchange_extension import (
    ICurrencyExchangeExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_currency_exchange_repository import (
    ICurrencyExchangeRepository,
)


class CurrencyExchangeRepository(ICurrencyExchangeRepository):

    __mongo_db_infrastructure: IMongoDbInfrastructure
    __collection: IMongoDbCollection
    __currency_exchange_extension: ICurrencyExchangeExtension

    @WitchDoctor.injection
    def __init__(
        self,
        mongo_db_infrastructure: IMongoDbInfrastructure,
        currency_exchange_extension: ICurrencyExchangeExtension,
    ):
        CurrencyExchangeRepository.__mongo_db_infrastructure = mongo_db_infrastructure
        CurrencyExchangeRepository.__collection = (
            CurrencyExchangeRepository.__mongo_db_infrastructure.require_collection(
                database=config("JAYA_DATABASE"),
                collection=config("CURRENCY_EXCHANGE_COLLECTION"),
            )
        )
        CurrencyExchangeRepository.__currency_exchange_extension = (
            currency_exchange_extension
        )

    @classmethod
    async def register_currency_exchange(
        cls, model: CurrencyExchangeModel
    ) -> CurrencyExchangeModel:
        try:
            async with cls.__collection.with_collection() as collection:
                await collection.insert_one(model.to_insert())

                return model

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToInsertException(
                message="Failed to insert currency exchange in database.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def get_currency_exchanges_by_user_id(
        cls, user_id: str
    ) -> List[CurrencyExchangeModel]:
        try:
            async with cls.__collection.with_collection() as collection:
                query = {"user_id": user_id}

                if result_list := await collection.find(query).to_list(length=None):
                    model_list = cls.__currency_exchange_extension.from_database_result_to_model_list(
                        result_list=result_list
                    )

                    return model_list

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Failed to retrieve currency exchanges in database.",
                original_error=original_exception,
            ) from original_exception
