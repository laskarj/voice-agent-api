from fastapi import APIRouter

from .tts.routes import router as tts_router
from .chat.routes import router as chat_router
from .transcribe.routes import router as transcribe_router


def get_router() -> APIRouter:
    v1_router = APIRouter(prefix='/v1', tags=['v1'])
    v1_router.include_router(tts_router)
    v1_router.include_router(chat_router)
    v1_router.include_router(transcribe_router)

    return v1_router
