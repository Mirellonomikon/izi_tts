import streamlit as st
import os
from typing import Optional

def load_custom_css():
    """Load custom CSS for purple theme enhancements"""
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_header():
    """Render application header"""
    st.markdown("""
    <div class="header-container">
        <h1>🎤 TTS Generator</h1>
        <p>Convert text to speech with customizable voice and model settings</p>
    </div>
    """, unsafe_allow_html=True)

def render_input_form() -> tuple:
    """
    Render input form and return user inputs
    Returns:
        Tuple of (text, voice, model, generate_clicked)
    """
    with st.form("tts_form", clear_on_submit=False):
        st.subheader("📝 Input Configuration")
        # Text input
        text_input = st.text_area(
            "Text to Convert",
            height=150,
            placeholder="Enter the text you want to convert to speech...",
            help="Type or paste the text you want to convert to audio"
        )
        col1, col2 = st.columns(2)
        with col1:
            voice_input = st.text_input(
                "Voice",
                value="Orus",
                placeholder="e.g., Orus, Nova, etc.",
                help="Enter the voice name for speech generation"
            )
        with col2:
            model_input = st.text_input(
                "Model",
                value="gemini-2.5-pro-preview-tts",
                placeholder="e.g., gemini-2.5-pro-preview-tts",
                help="Enter the TTS model name"
            )
        generate_button = st.form_submit_button(
            "🎵 Generate Speech",
            use_container_width=True,
            type="primary"
        )
        return text_input, voice_input, model_input, generate_button

def display_message(message_type: str, message: str):
    """Display status messages"""
    if message_type == "success":
        st.success(message)
    elif message_type == "error":
        st.error(message)
    elif message_type == "warning":
        st.warning(message)
    elif message_type == "info":
        st.info(message)

def render_audio_player(audio_file_path: str):
    """Render audio player for generated speech"""
    if audio_file_path and os.path.exists(audio_file_path):
        st.subheader("🔊 Generated Audio")
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav")
        # Download button
        st.download_button(
            label="📥 Download Audio",
            data=audio_bytes,
            file_name="generated_speech.wav",
            mime="audio/wav",
            use_container_width=True
        )

def cleanup_temp_file(file_path: Optional[str]):
    """Clean up temporary audio file"""
    if file_path and os.path.exists(file_path):
        try:
            os.unlink(file_path)
        except Exception:
            pass  # Silently handle cleanup errors
