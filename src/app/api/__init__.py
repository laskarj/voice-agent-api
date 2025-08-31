from fastapi import FastAPI, APIRouter
from . import v1


def setup(app: FastAPI) -> None:
    api_router = APIRouter(prefix='/api')
    v1_router = v1.get_router()
    api_router.include_router(v1_router)

    app.include_router(api_router)
