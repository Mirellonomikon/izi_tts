import os
import tempfile
import wave
from typing import Optional, Tuple, List
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class GeminiTTSService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        self.client = genai.Client(api_key=self.api_key)

        # Available models
        self.available_models = [
            "gemini-2.5-flash-preview-tts",
            "gemini-2.5-pro-preview-tts"
        ]

        # Available voices with descriptions
        self.available_voices = [
            ("Zephyr", "Bright"),
            ("Kore", "Firm"),
            ("Orus", "Firm"),
            ("Autonoe", "Bright"),
            ("Umbriel", "Easy-going"),
            ("Erinome", "Clear"),
            ("Laomedeia", "Upbeat"),
            ("Schedar", "Even"),
            ("Achird", "Friendly"),
            ("Sadachbia", "Lively"),
            ("Puck", "Upbeat"),
            ("Fenrir", "Excitable"),
            ("Aoede", "Breezy"),
            ("Enceladus", "Breathy"),
            ("Algieba", "Smooth"),
            ("Algenib", "Gravelly"),
            ("Achernar", "Soft"),
            ("Gacrux", "Mature"),
            ("Zubenelgenubi", "Casual"),
            ("Sadaltager", "Knowledgeable"),
            ("Charon", "Informative"),
            ("Leda", "Youthful"),
            ("Callirrhoe", "Easy-going"),
            ("Iapetus", "Clear"),
            ("Despina", "Smooth"),
            ("Rasalgethi", "Informative"),
            ("Alnilam", "Firm"),
            ("Pulcherrima", "Forward"),
            ("Vindemixtrix", "Gentle"),
            ("Sulafat", "Warm")
        ]
    def get_available_models(self) -> List[str]:
        """Get list of available TTS models"""
        return self.available_models.copy()
    def get_available_voices(self) -> List[Tuple[str, str]]:
        """Get list of available voices with descriptions"""
        return self.available_voices.copy()
    def wave_file(self, filename: str, pcm: bytes, channels: int = 1, rate: int = 24000, sample_width: int = 2):
        """Create wave file from PCM data"""
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm)
    def generate_speech(self, text: str, voice: str, model: str) -> Tuple[bool, str, Optional[str]]:
        """
        Generate speech from text using Gemini TTS API

        Returns:
            Tuple of (success: bool, message: str, audio_file_path: Optional[str])
        """
        if not text.strip():
            return False, "Text input cannot be empty", None
        if voice not in [v[0] for v in self.available_voices]:
            return False, f"Invalid voice selection: {voice}", None
        if model not in self.available_models:
            return False, f"Invalid model selection: {model}", None
        try:
            # Generate content with TTS
            response = self.client.models.generate_content(
                model=model,
                contents=text.strip(),
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice,
                            )
                        )
                    ),
                )
            )
            # Extract audio data
            if (response.candidates and
                len(response.candidates) > 0 and
                response.candidates[0].content.parts and
                len(response.candidates[0].content.parts) > 0):

                audio_data = response.candidates[0].content.parts[0].inline_data.data

                # Create temporary file
                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".wav",
                    prefix="gemini_tts_"
                )
                # Save as wave file
                self.wave_file(temp_file.name, audio_data)

                return True, "Audio generated successfully", temp_file.name
            else:
                return False, "No audio data received from API", None
        except Exception as e:
            return False, f"Generation error: {str(e)}", None
