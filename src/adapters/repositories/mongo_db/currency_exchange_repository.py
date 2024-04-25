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
)
from src.domain.models.currency_exchange_model import CurrencyExchangeModel
from src.externals.infrastructures.mongo_db.exceptions.mongo_db_base_infrastructure_exception import (
    MongoDbBaseInfrastructureException,
)
from src.use_cases.ports.repositories.mongo_db.i_currency_exchange_repository import (
    ICurrencyExchangeRepository,
)


class CurrencyExchangeRepository(ICurrencyExchangeRepository):

    __mongo_db_infrastructure: IMongoDbInfrastructure
    __collection: IMongoDbCollection

    @WitchDoctor.injection
    def __init__(
        self,
        mongo_db_infrastructure: IMongoDbInfrastructure,
    ):
        CurrencyExchangeRepository.__mongo_db_infrastructure = mongo_db_infrastructure
        CurrencyExchangeRepository.__collection = (
            CurrencyExchangeRepository.__mongo_db_infrastructure.require_collection(
                database=config("JAYA_DATABASE"),
                collection=config("CURRENCY_EXCHANGE_COLLECTION"),
            )
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
