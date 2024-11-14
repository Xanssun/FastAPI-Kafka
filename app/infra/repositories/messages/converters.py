from domain.entities.messages import Chat, Message


def convert_message_to_document(message: Message):
    return {
        'oid': message.oid,
        'text': message.text.as_generic_type(),
    }


def convert_entity_to_document(chat: Chat):
    return {
        'oid': chat.oid,
        'title': chat.title.as_generic_type(),
        'created_at': chat.created_at,
        'messages': [convert_message_to_document(message) for message in chat.message],
    }
