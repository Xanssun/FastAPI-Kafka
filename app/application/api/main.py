from fastapi import FastAPI


def create_app():
    return FastAPI(
        title = 'Simple chat',
        docs_url = '/api/docs',
        description = 'Simple chat'
    )
