import pytest
import json
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_websocket_connection(client):
    """Test WebSocket connection establishment."""
    with client.websocket_connect("/api/chat/stream") as websocket:
        assert websocket is not None

@pytest.mark.asyncio
async def test_websocket_message_flow(client):
    """Test complete message flow through WebSocket."""
    with patch("core.llm.service.LLMService.get_completion", return_value="Test response"), \
         patch("core.tts.service.TTSService.text_to_speech", return_value=b"mock audio data"):
        
        with client.websocket_connect("/api/chat/stream") as websocket:
            # Send message
            websocket.send_text(json.dumps({
                "type": "text",
                "content": "Test message"
            }))
            
            # Receive text response
            text_response = websocket.receive_text()
            text_data = json.loads(text_response)
            assert text_data["type"] == "text"
            assert text_data["content"] == "Test response"
            
            # Receive audio response
            audio_response = websocket.receive_text()
            audio_data = json.loads(audio_response)
            assert audio_data["type"] == "audio"
            assert audio_data["content"] == "bW9jayBhdWRpbyBkYXRh"  # base64 of "mock audio data"

@pytest.mark.asyncio
async def test_websocket_error_handling(client):
    """Test WebSocket error handling."""
    with patch("core.llm.service.LLMService.get_completion", side_effect=Exception("Test error")):
        with client.websocket_connect("/api/chat/stream") as websocket:
            # Send message
            websocket.send_text(json.dumps({
                "type": "text",
                "content": "Test message"
            }))
            
            # Receive error response
            response = websocket.receive_text()
            error_data = json.loads(response)
            assert "error" in error_data
            assert "Test error" in error_data["error"] 