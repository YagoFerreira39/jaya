import loglifos  # pylint: disable=E0401
import meeseeks
from decouple import config
from motor.motor_asyncio import (  # pylint: disable=E0401
    AsyncIOMotorClient,
)
from pymongo.errors import (  # pylint: disable=E0401
    ConfigurationError,
    ConnectionFailure,
)

from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbCollection,
    IMongoDbInfrastructure,
)
from src.externals.infrastructures.mongo_db.exceptions.mongo_db_infrastructure_exceptions import (
    MongoDbInfrastructureUnableToConnectError,
    MongoDbInfrastructureUnexpectedError,
)
from src.externals.infrastructures.mongo_db.mongo_db_collection import MongoDbCollection


@meeseeks.OnlyOne()
class MongoDbInfrastructure(IMongoDbInfrastructure):
    def __init__(self):
        self._connection_string = config("MONGODB_STRING_CONNECTION")
        loglifos.debug(
            msg="Creating InfraMongoDb", connection_string=self._connection_string
        )
        self._client: AsyncIOMotorClient = None

    @property
    def client(self):
        if self._client is None:
            loglifos.debug(
                msg="Creating a AsyncIOMotorClient instance",
                _str_connection=self._connection_string,
            )
            try:
                self._client = AsyncIOMotorClient(self._connection_string)
            except (
                ConfigurationError,
                ConnectionFailure,
            ) as original_error:
                loglifos.debug(msg="Cleaning AsyncIOMotorClient client")
                raise MongoDbInfrastructureUnableToConnectError(
                    message=f"Fail to connect to uri: {self._connection_string}",
                    original_error=original_error,
                ) from original_error
            except Exception as original_error:
                raise MongoDbInfrastructureUnexpectedError(
                    message="So seed so far! see original_error",
                    original_error=original_error,
                ) from original_error
        return self._client

    def require_collection(self, database: str, collection: str) -> IMongoDbCollection:
        return MongoDbCollection(
            client=self.client, database=database, collection=collection
        )
