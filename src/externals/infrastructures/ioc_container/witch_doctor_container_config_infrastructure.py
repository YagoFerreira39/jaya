from witch_doctor import WitchDoctor, InjectionType

from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)
from src.adapters.ports.infrastructures.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)
from src.externals.infrastructures.mongo_db.mongo_db_collection import MongoDbCollection
from src.externals.infrastructures.mongo_db.mongo_db_infrastructure import (
    MongoDbInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
    IIocContainerConfigInfrastructure,
)


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")

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

        return infrastructures_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        return extensions_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_repositories_container()
        cls.__create_extensions_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container("use_cases")
        WitchDoctor.load_container("infrastructures")
        WitchDoctor.load_container("repositories")
        WitchDoctor.load_container("extensions")

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
