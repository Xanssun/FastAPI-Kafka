from dataclasses import dataclass

from logic.exception.base import LogicException


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f'Чат с заголовком "{self.title}" уже существует.'
 