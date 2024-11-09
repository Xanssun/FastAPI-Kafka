from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text
    # _hash_ = BaseEntity.__hash__


@dataclass
class Chat(BaseEntity):
    title: Title
    # _hash_ = BaseEntity.__hash__
    message: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message):
        self.message.add(message)
