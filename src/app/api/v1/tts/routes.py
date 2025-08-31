import io

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.api.v1.tts.schemas import TTSRequest

router = APIRouter(prefix="/tts")


@router.post("/")
async def text_to_speech(request: TTSRequest) -> StreamingResponse:
    # In a real implementation, you would convert the text to speech.
    # For now, we'll return a dummy audio file.
    dummy_audio_bytes = b"dummy_audio_content"
    return StreamingResponse(io.BytesIO(dummy_audio_bytes), media_type="audio/mpeg")
