import openai
from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse

from app.api.v1.transcribe.schemas import TranscribeResponse
from app.config import Config
from app.dependencies import Stub

router = APIRouter(prefix="/transcribe")


@router.post("/", response_model=TranscribeResponse)
async def transcribe_audio(
        file: UploadFile = File(...),
        config: Config = Depends(Stub(Config))
) -> TranscribeResponse:
    try:
        openai.api_key = config.OPENAI_API_KEY
        with open("temp_audio.wav", "wb") as f:
            f.write(await file.read())

        with open("temp_audio.wav", "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        return TranscribeResponse(text=transcript.text)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
