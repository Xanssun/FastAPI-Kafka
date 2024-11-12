from infra.repositories.messages import (BaseChatRepository,
                                         MemoryChatRepository)
from logic.init import init_mediator
from logic.mediator import Mediator
from pytest import fixture


@fixture(scope='package')
def chat_repository():
    return MemoryChatRepository()


@fixture(scope='package')
def mediator(chat_repository: BaseChatRepository):
    mediator = Mediator()
    init_mediator(mediator=mediator, chat_repository=chat_repository)

    return mediator
