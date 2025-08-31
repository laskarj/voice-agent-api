from fastapi import  FastAPI

from app.config import Config
from .providers import get_config
from .stub import Stub


def setup(app: FastAPI):
    app.dependency_overrides[Stub(Config)] = get_config
