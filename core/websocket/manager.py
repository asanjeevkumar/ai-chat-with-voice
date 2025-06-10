from typing import Dict, Any
from fastapi import WebSocket


class ConnectionManager:
    """Manages WebSocket connections."""

    def __init__(self):
        self.active_connections: Dict[WebSocket, Any] = {}

    async def connect(self, websocket: WebSocket):
        """Accept and store a new WebSocket connection."""
        await websocket.accept()
        self.active_connections[websocket] = {}

    def disconnect(self, websocket: WebSocket):
        """Remove a WebSocket connection."""
        if websocket in self.active_connections:
            del self.active_connections[websocket]

    async def send_error(self, websocket: WebSocket, error_message: str):
        """Send an error message to a specific WebSocket connection."""
        await websocket.send_text(error_message)


connection_manager = ConnectionManager()
