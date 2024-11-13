from application.api.messages.handlers import router as message_router
from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title = 'Simple chat',
        docs_url = '/api/docs',
        description = 'Simple chat',
        debug = True,
    )
    app.include_router(message_router, prefix='/chat')

    return app
