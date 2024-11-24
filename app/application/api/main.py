from contextlib import asynccontextmanager

from application.api import lifespan
from application.api.lifespan import close_kafka, start_kafka
from application.api.messages.handlers import router as message_router
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_kafka()
    yield
    await close_kafka()


def create_app():
    app = FastAPI(
        title = 'Simple chat',
        docs_url = '/api/docs',
        description = 'Simple chat',
        debug = True,
        lifespan=lifespan
    )
    app.include_router(message_router, prefix='/chat')

    return app
