from abc import abstractmethod, ABC

from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)


class IMongoDbInfrastructure(ABC):
    @abstractmethod
    def require_collection(self, database: str, collection: str) -> IMongoDbCollection:
        pass
