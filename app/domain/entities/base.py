from abc import ABC
from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from domain.events.base import BaseEvent


@dataclass()
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    _events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True,
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )

    def __hash__(self):
        return hash(self.oid)
    
    def __eq__(self, __value: 'BaseEntity'):
        return self.oid == __value.oid

    def register_event(self, event: BaseEvent):
        self._events.append(event)

    def pull_events(self):
        reg_events = copy(self._events)
        self._events.clear()
        return reg_events
