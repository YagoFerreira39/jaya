import loglifos
from decouple import config  # pylint: disable=E0401

from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class LoglifosConfigInfrastructure(ILogsConfigInfrastructure):
    @classmethod
    def config_logs(cls):
        loglifos.set_config(log_level=int(config("LOG_LEVEL")))
