from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(default='localhost', alias='MONGO_DB_CONNECTION_URI')
    mongodb_chat_database: str = Field(default='chat', alias='MONGODB_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGODB_CHAT_COLLECTION')
    mongodb_messages_collection: str = Field(default='messages', alias='MONGODB_MESSAGE_COLLECTION')
    
    new_chats_event_topic: str = Field(default='new-chats-topic')
    new_message_received_topic: str = Field(default='new-message-received-topic')

    kafka_url: str = Field(default='kafka:29092', alias='KAFKA_URL')
