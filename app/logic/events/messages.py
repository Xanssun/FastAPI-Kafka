from dataclasses import dataclass

from domain.events.messages import NewChatCreatedEvent
from infra.message_brokers.converters import convert_event_to_broker_message
from logic.events.base import EventHandler


@dataclass()
class NewChatCreatedEventHandler(EventHandler[NewChatCreatedEvent, None]):

    async def handle(self, event: NewChatCreatedEvent):
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event),
            key=str(event.event_id).encode(),
        )
        print(f'Обработали событие {event.chat_title}')
