# from application.api.dependencies.containers import container
from application.api.messages.schemas import (CreateChatRequestSchema,
                                              CreateChatResponseSchema)
from domain.exception.base import ApplicationException
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from logic.commands.messages import CreateChatCommand
from logic.init import init_container
from logic.mediator import Mediator

router = APIRouter(
    tags=['chat'],
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='Создает новый чат, если чат с таким названием существует, то возвращается 400',
    responses={
        status.HTTP_201_CREATED: {'model': CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': str},
    },
)
async def create_chat_handler(
    schema: CreateChatRequestSchema,
    container=Depends(init_container)
):
    ''' Создать новый чат. '''
    mediator: Mediator = container.resolve(Mediator)

    try:
        chat, *_ = await mediator.handle_command(CreateChatCommand(title=schema.title))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return CreateChatResponseSchema.from_entity(chat)
