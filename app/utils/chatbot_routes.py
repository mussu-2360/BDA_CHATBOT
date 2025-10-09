from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.bot_logic import get_bot_response


router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    reply = get_bot_response(request.message)
    return {"reply": reply}


