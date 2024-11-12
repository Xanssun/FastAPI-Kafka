from infra.repositories.messages import MemoryChatRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from logic.mediator import Mediator


def init_mediator(
        mediator: Mediator,
        chat_repository: MemoryChatRepository,
):
    mediator.register_command(
        CreateChatCommand,
        [CreateChatCommandHandler(chat_repository=chat_repository)],
    )
