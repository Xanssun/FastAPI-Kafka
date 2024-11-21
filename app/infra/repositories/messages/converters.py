from domain.entities.messages import Chat, Message
from domain.values.messages import Text, Title


def convert_message_to_document(message: Message):
    return {
        'oid': message.oid,
        'text': message.text.as_generic_type(),
        'created_at': message.created_at,
    }

def convert_chat_entity_to_document(chat: Chat):
    return {
        'oid': chat.oid,
        'title': chat.title.as_generic_type(),
        'created_at': chat.created_at,
    }

def convert_message_document_to_entity(message_document) -> Message:
    return Message(
        text=Text(value=message_document['text']),
        oid=message_document['oid'],
        created_at=message_document['created_at'],
    )

def convert_chat_document_to_entity(chat_document) -> Chat:
    return Chat(
        oid=chat_document['oid'],
        title=Title(value=chat_document['title']),
        created_at=chat_document['created_at'],
    )
