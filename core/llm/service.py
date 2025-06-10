from openai import OpenAI
from core.config.settings import settings


class LLMService:
    """Service for handling LLM interactions."""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME

    async def get_completion(self, text: str) -> str:
        """
        Get a completion from the LLM.

        Args:
            text: The input text to send to the LLM

        Returns:
            The LLM's response text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=[{"role": "user", "content": text}]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error getting LLM completion: {str(e)}")


llm_service = LLMService()
