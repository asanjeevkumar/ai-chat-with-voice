import pytest
from unittest.mock import AsyncMock, patch
from core.tts.service import TTSService


@pytest.fixture
def tts_service():
    return TTSService()


@pytest.mark.asyncio
async def test_text_to_speech_success(tts_service):
    """Test successful text to speech conversion."""
    mock_response = AsyncMock()
    mock_response.content = b"mock audio data"

    with patch.object(
        tts_service.client.audio.speech, "create", return_value=mock_response
    ):
        response = await tts_service.text_to_speech("Test text")
        assert response == b"mock audio data"


@pytest.mark.asyncio
async def test_text_to_speech_error(tts_service):
    """Test error handling in text to speech conversion."""
    with patch.object(
        tts_service.client.audio.speech, "create", side_effect=Exception("API Error")
    ):
        with pytest.raises(Exception) as exc_info:
            await tts_service.text_to_speech("Test text")
        assert "Error converting text to speech" in str(exc_info.value)
