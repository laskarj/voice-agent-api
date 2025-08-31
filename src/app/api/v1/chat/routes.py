from fastapi import APIRouter

from app.api.v1.chat.schemas import ChatResponse, ChatRequest

router = APIRouter(prefix='/chat')


@router.post("/", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest) -> ChatResponse:
    # In a real implementation, you would process the text with a chat model.
    # For now, we'll just return a dummy response.
    return ChatResponse(text=f"You said: {request.text}")
