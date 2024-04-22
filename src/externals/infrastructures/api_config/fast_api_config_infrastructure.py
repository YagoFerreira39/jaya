from fastapi import FastAPI

from src.externals.ports.infrastructures.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigStructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
    IIocContainerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class FastAPIConfigInfrastructure(IApiConfigInfrastructure):
    def __init__(
        self,
        http_server_config_infrastructure: IHttpServerConfigStructure,
        ioc_container_config_infrastructure: IIocContainerConfigInfrastructure,
        logs_config_infrastructure: ILogsConfigInfrastructure,
    ):
        self.__http_server_config_infrastructure = http_server_config_infrastructure
        self.__ioc_container_config_infrastructure = ioc_container_config_infrastructure
        self.__logs_config_infrastructure = logs_config_infrastructure

    def config_api(self) -> FastAPI:
        app = self.__http_server_config_infrastructure.config_http_server()
        self.__ioc_container_config_infrastructure.build_ioc_container()
        self.__logs_config_infrastructure.config_logs()

        return app
