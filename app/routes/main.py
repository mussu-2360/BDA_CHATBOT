from fastapi import FastAPI
from app.routes.chatbot_routes import router as chatbot_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.chatbot_routes import router as chatbot_router
import os

# Initialize FastAPI app
app = FastAPI(
    title="BDA Chatbot",
    description="An intelligent chatbot for Bhopal Development Authority using FastAPI",
    version="1.0.0"
)

# Register chatbot routes
app.include_router(chatbot_router, prefix="/api/chatbot", tags=["Chatbot"])


# Mount static folder
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def home():
    return FileResponse(os.path.join(static_dir, "chat.html"))


