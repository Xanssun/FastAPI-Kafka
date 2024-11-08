from dataclasses import dataclass

from domain.exception.messages import TextTooLongException
from domain.values.base import BaseVelueObject


@dataclass(frozen=True)
class Text(BaseVelueObject):
    value: str

    def validate(self):
        if len(self.value) > 255:
            raise TextTooLongException(self.value)
    
    def as_generic_type(self):
        return str(self.value)
