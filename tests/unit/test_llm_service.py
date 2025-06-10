import pytest
from unittest.mock import AsyncMock, patch
from core.llm.service import LLMService

@pytest.fixture
def llm_service():
    return LLMService()

@pytest.mark.asyncio
async def test_get_completion_success(llm_service):
    """Test successful completion from LLM."""
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="Test response"))]
    
    with patch.object(llm_service.client.chat.completions, 'create', return_value=mock_response):
        response = await llm_service.get_completion("Test input")
        assert response == "Test response"

@pytest.mark.asyncio
async def test_get_completion_error(llm_service):
    """Test error handling in LLM completion."""
    with patch.object(llm_service.client.chat.completions, 'create', side_effect=Exception("API Error")):
        with pytest.raises(Exception) as exc_info:
            await llm_service.get_completion("Test input")
        assert "Error getting LLM completion" in str(exc_info.value) 