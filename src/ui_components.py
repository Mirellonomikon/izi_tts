import streamlit as st
import os
from typing import Optional, List, Tuple
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
        <h1>🎤 Gemini TTS Generator</h1>
        <p>Convert text to speech using Google's Gemini TTS models</p>
    </div>
    """, unsafe_allow_html=True)
def render_input_form(available_voices: List[Tuple[str, str]], available_models: List[str]) -> tuple:
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
            # Voice dropdown with descriptions
            voice_options = [f"{voice} ({desc})" for voice, desc in available_voices]
            voice_selection = st.selectbox(
                "Voice",
                options=voice_options,
                index=1,  # Default to Kore
                help="Select the voice for speech generation"
            )
            # Extract just the voice name
            selected_voice = voice_selection.split(" (")[0]
        with col2:
            model_selection = st.selectbox(
                "Model",
                options=available_models,
                index=0,  # Default to flash model
                help="Select the TTS model to use"
            )
        generate_button = st.form_submit_button(
            "🎵 Generate Speech",
            use_container_width=True,
            type="primary"
        )
        return text_input, selected_voice, model_selection, generate_button
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
            file_name="gemini_tts_output.wav",
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
