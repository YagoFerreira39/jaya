import uvicorn
from decouple import config
from fastapi import FastAPI
from pyfiglet import print_figlet

from src.externals.infrastructures.api_config.fast_api_config_infrastructure import (
    FastAPIConfigInfrastructure,
)
from src.externals.infrastructures.http_config.fast_api_http_server_config_infrastructure import (
    FastApiHttpServerConfigInfrastructure,
)
from src.externals.infrastructures.ioc_container.witch_doctor_container_config_infrastructure import (
    WitchDoctorContainerConfigInfrastructure,
)
from src.externals.infrastructures.logs.loglifos_config_infrastructure import (
    LoglifosConfigInfrastructure,
)


def config_app() -> FastAPI:
    http_server_config_infrastructure = FastApiHttpServerConfigInfrastructure()
    ioc_container_config_infrastructure = WitchDoctorContainerConfigInfrastructure()
    logs_config_infrastructure = LoglifosConfigInfrastructure()

    fast_api_config_infrastructure = FastAPIConfigInfrastructure(
        http_server_config_infrastructure=http_server_config_infrastructure,
        ioc_container_config_infrastructure=ioc_container_config_infrastructure,
        logs_config_infrastructure=logs_config_infrastructure,
    )

    return fast_api_config_infrastructure.config_api()


if __name__ == "__main__":
    host = config("SERVER_HOST")
    port = int(config("SERVER_PORT"))
    app = config_app()

    print(f"Server is ready at URL {host}:{port}")
    print_figlet(text="Jaya", colors="174;55;255", width=260)

    uvicorn.run(app, host=host, port=port)
