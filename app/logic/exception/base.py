from dataclasses import dataclass

from domain.exception.base import ApplicationException


@dataclass(eq=False)
class LogicException(ApplicationException):

    @property
    def message(self):
        return 'В обработки запроса возникла ошибка'
