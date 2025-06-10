import json
import base64
from fastapi import WebSocket, WebSocketDisconnect
from core.websocket.manager import connection_manager
from core.llm.service import llm_service
from core.tts.service import tts_service


async def handle_websocket(websocket: WebSocket):
    """
    Handle WebSocket connections and message processing.

    Args:
        websocket: The WebSocket connection
    """
    await connection_manager.connect(websocket)
    try:
        while True:
            # Receive message from client
            message = await websocket.receive_text()
            message_data = json.loads(message)

            if message_data.get("type") != "text":
                error_message = {"error": "Invalid message type. Expected 'text'."}
                await connection_manager.send_error(websocket, json.dumps(error_message))
                continue

            try:
                # Get response from LLM
                response_text = await llm_service.get_completion(message_data["content"])

                # Send text response
                text_response = {
                    "type": "text",
                    "content": response_text
                }
                await websocket.send_text(json.dumps(text_response))

                # Convert response to speech
                audio_data = await tts_service.text_to_speech(response_text)

                # Base64 encode the audio data
                audio_b64 = base64.b64encode(audio_data).decode('utf-8')

                # Send audio response
                audio_response = {
                    "type": "audio",
                    "content": audio_b64
                }
                await websocket.send_text(json.dumps(audio_response))

            except Exception as e:
                # Send error message back to client
                error_message = {"error": str(e)}
                await connection_manager.send_error(websocket, json.dumps(error_message))

    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
