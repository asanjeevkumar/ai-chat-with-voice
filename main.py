from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import uvicorn
from core.config.settings import settings
from core.websocket.router import handle_websocket

# Initialize FastAPI app
app = FastAPI(title="AI Chat with Voice")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """Redirect root path to the static index.html file."""
    return RedirectResponse(url="/static/index.html")


@app.websocket("/api/chat/stream")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for streaming chat responses with voice synthesis."""
    await handle_websocket(websocket)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
