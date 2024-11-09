from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text


@dataclass
class Chat(BaseEntity):
    title: Title
    message: set[Message] = field(
        default_factory=set, # не уверен что лучше оставить set
        kw_only=True,
    )
