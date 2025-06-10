from openai import OpenAI
from core.config.settings import settings


class TTSService:
    """Service for handling text-to-speech conversion."""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.TTS_MODEL
        self.voice = settings.TTS_VOICE

    async def text_to_speech(self, text: str) -> bytes:
        """
        Convert text to speech.

        Args:
            text: The text to convert to speech

        Returns:
            The audio data as bytes
        """
        try:
            response = self.client.audio.speech.create(
                model=self.model, voice=self.voice, input=text
            )
            return response.content
        except Exception as e:
            raise Exception(f"Error converting text to speech: {str(e)}")


tts_service = TTSService()
