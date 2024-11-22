from application.api.messages.filters import GetMessagesFilters
from application.api.messages.schemas import (ChatDetailSchema,
                                              CreateChatRequestSchema,
                                              CreateChatResponseSchema,
                                              CreateMessageResponseSchema,
                                              CreateMessageSchema,
                                              GetMessagesQueryResponseSchema,
                                              MessageDetailSchema)
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from logic.commands.messages import CreateChatCommand, CreateMessageCommand
from logic.init import init_container
from logic.mediator import Mediator
from logic.queries.messages import GetChatDetailQuery, GetMessagesQuery
from punq import Container

router = APIRouter(
    tags=['chat'],
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='Создает новый чат, если чат с таким названием существует, то возвращается 400',
    responses={
        status.HTTP_201_CREATED: {'model': CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_chat_handler(
    schema: CreateChatRequestSchema,
    container: Container = Depends(init_container)
):
    ''' Создать новый чат. '''
    mediator: Mediator = container.resolve(Mediator)

    try:
        chat, *_ = await mediator.handle_command(CreateChatCommand(title=schema.title))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return CreateChatResponseSchema.from_entity(chat)

@router.post(
    '/{chat_oid}/messages',
    status_code=status.HTTP_201_CREATED,
    description='Добавить новое сообщение в чат',
    responses={
        status.HTTP_201_CREATED: {'model': CreateMessageResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    }
)
async def create_message_handler(
    chat_oid: str,
    schema: CreateMessageSchema,
    container: Container = Depends(init_container),
):
    ''' добавить новое сообщение в чат. '''
    mediator: Mediator = container.resolve(Mediator)

    try:
        message, *_ = await mediator.handle_command(CreateMessageCommand(text=schema.text, chat_oid=chat_oid))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateMessageResponseSchema.from_entity(message)

@router.get(
    '/{chat_oid}/',
    status_code=status.HTTP_200_OK,
    description='Получить чат по ID',
    responses={
        status.HTTP_201_CREATED: {'model': ChatDetailSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def get_chat_handler(
    chat_oid: str,
    container: Container = Depends(init_container),
) -> ChatDetailSchema:
    mediator: Mediator = container.resolve(Mediator)

    try:
        chat = await mediator.handle_query(GetChatDetailQuery(chat_oid=chat_oid))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return ChatDetailSchema.from_entity(chat)

@router.get(
    '/{chat_oid}/messages/',
    status_code=status.HTTP_200_OK,
    description='Получить все сообщения в чате',
    responses={
        status.HTTP_201_CREATED: {'model': GetMessagesQueryResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def get_chat_messages_handler(
    chat_oid: str,
    filters: GetMessagesFilters = Depends(),
    container: Container = Depends(init_container),
):
    mediator: Mediator = container.resolve(Mediator)

    try:
        messages, count = await mediator.handle_query(
            GetMessagesQuery(chat_oid=chat_oid, filters=filters.to_infta())
        )
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return GetMessagesQueryResponseSchema(
        count=count,
        limit=filters.limit,
        offset=filters.offset,
        items=[MessageDetailSchema.from_entity(message) for message in messages],
    )
