from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(default='localhost', alias='MONGO_DB_CONNECTION_URI')
    mongodb_chat_database: str = Field(default='chat', alias='MONGO_DB_ADMIN_USERNAME')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGO_DB_ADMIN_PASSWORD')
