from src.adapters.repositories.mongo_db.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.mongo_db.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)


class FailToInsertException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.FAIL_TO_INSERT_ERROR


class FailToRetrieveInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.FAIL_TO_RETRIEVE_INFORMATION_ERROR
