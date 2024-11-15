from datetime import datetime
from typing import Iterable

from domain.entities.messages import Chat, Message
from pydantic import BaseModel


class CreateChatRequestSchema(BaseModel):
    title: str


class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str

    @classmethod
    def from_entity(cls, chat: Chat):
        return cls(
            oid = chat.oid,
            title = chat.title.as_generic_type(),
        )


class CreateMessageSchema(BaseModel):
    text: str


class CreateMessageResponseSchema(BaseModel):
    text: str
    oid: str

    @classmethod
    def from_entity(cls, message: Message):
        return cls(
            text = message.text.as_generic_type(),
            oid = message.oid,
        )


class MessageDetailSchema(BaseModel):
    oid: str
    text: str
    created_at: datetime


class ChatResponseSchema(BaseModel):
    oid: str
    title: str
    created_at: datetime

    @classmethod
    def from_entity(cls, chat: Chat):
        return cls(
            oid = chat.oid,
            title = chat.title.as_generic_type(),
            created_at = chat.created_at,
        )
