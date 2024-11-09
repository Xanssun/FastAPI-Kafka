from dataclasses import dataclass

from domain.exception.base import ApplicationException


@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Текст сообщения "{self.text}" слишком длинный. Максимальная длина - 255 символов.'



@dataclass(eq=False)
class EmptyTextError(ApplicationException):

    @property
    def message(self):
        return f'Текст сообщения не может быть пустым'
