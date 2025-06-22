import requests
import os
import tempfile
from typing import Optional, Tuple
from dotenv import load_dotenv

load_dotenv()

class TTSService:
    def __init__(self):
        self.api_key = os.getenv("ELECTRONHUB_API_KEY")
        self.base_url = "https://api.electronhub.ai/v1/audio/speech"

        if not self.api_key:
            raise ValueError("API_KEY not found in environment variables")

    def generate_speech(self, text: str, voice: str, model: str) -> Tuple[bool, str, Optional[str]]:
        """
        Generate speech from text using the TTS API

        Returns:
            Tuple of (success: bool, message: str, audio_file_path: Optional[str])
        """
        if not text.strip():
            return False, "Text input cannot be empty", None

        if not voice.strip():
            return False, "Voice selection cannot be empty", None

        if not model.strip():
            return False, "Model name cannot be empty", None

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": model.strip(),
            "input": text.strip(),
            "voice": voice.strip()
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                # Create temporary file
                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".wav",
                    prefix="tts_"
                )

                with temp_file as f:
                    f.write(response.content)
                    temp_path = f.name

                return True, "Audio generated successfully", temp_path

            else:
                error_msg = f"API Error {response.status_code}: {response.text}"
                return False, error_msg, None

        except requests.exceptions.Timeout:
            return False, "Request timed out. Please try again.", None
        except requests.exceptions.ConnectionError:
            return False, "Connection error. Check your internet connection.", None
        except Exception as e:
            return False, f"Unexpected error: {str(e)}", None
