import streamlit as st
import atexit
from tts_service import TTSService
from ui_components import (
    load_custom_css,
    render_header,
    render_input_form,
    display_message,
    render_audio_player,
    cleanup_temp_file
)
# Page configuration
st.set_page_config(
    page_title="TTS Generator",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="collapsed"
)
def initialize_session_state():
    """Initialize session state variables"""
    if 'current_audio_file' not in st.session_state:
        st.session_state.current_audio_file = None
    if 'tts_service' not in st.session_state:
        try:
            st.session_state.tts_service = TTSService()
        except ValueError as e:
            st.error(f"Configuration Error: {e}")
            st.info("Please ensure your API key is set in the .env file")
            st.stop()
def cleanup_on_exit():
    """Clean up temporary files on application exit"""
    if hasattr(st.session_state, 'current_audio_file'):
        cleanup_temp_file(st.session_state.current_audio_file)
def main():
    """Main application function"""
    # Initialize
    initialize_session_state()
    load_custom_css()

    # Register cleanup function
    atexit.register(cleanup_on_exit)

    # Render UI
    render_header()

    # Input form
    text_input, voice_input, model_input, generate_clicked = render_input_form()

    # Handle form submission
    if generate_clicked:
        if not text_input.strip():
            display_message("warning", "Please enter some text to convert to speech.")
        else:
            with st.spinner("🔄 Generating speech... Please wait."):
                # Clean up previous audio file
                cleanup_temp_file(st.session_state.current_audio_file)
                st.session_state.current_audio_file = None

                # Generate new audio
                success, message, audio_file = st.session_state.tts_service.generate_speech(
                    text_input, voice_input, model_input
                )

                if success:
                    st.session_state.current_audio_file = audio_file
                    display_message("success", message)
                else:
                    display_message("error", message)

    # Display audio player if available
    if st.session_state.current_audio_file:
        render_audio_player(st.session_state.current_audio_file)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #9146FF; font-size: 0.9em;'>"
        "🤖 Powered by Coral Technology • Built with Streamlit"
        "</div>",
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()
