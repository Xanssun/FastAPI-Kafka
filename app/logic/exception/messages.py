from dataclasses import dataclass

from logic.exception.base import LogicException


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f'Чат с заголовком "{self.title}" уже существует.'


@dataclass(eq=False)
class ChatNotFoundException(LogicException):
    chat_oid: str

    @property
    def message(self):
        return f'Чат с таким {self.chat_oid=} не найден'
