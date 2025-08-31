from fastapi import FastAPI

from app import api, dependencies


def create_app() -> FastAPI:
    _app = FastAPI(root_path="/api")
    dependencies.setup(_app)
    api.setup(_app)
    return _app

app = create_app()
