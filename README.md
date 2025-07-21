# 🎤 Izi TTS - Gemini Text-to-Speech Generator

A beautiful and intuitive Streamlit web application that converts text to speech using Google's Gemini 2.5 TTS models.

## ✨ Features

- **Multiple Gemini TTS Models**: Choose between `gemini-2.5-flash-preview-tts` and `gemini-2.5-pro-preview-tts`
- **30 Unique Voices**: Wide variety of voices with different characteristics (bright, firm, upbeat, smooth, etc.)
- **Clean UI**: Purple-themed interface built with Streamlit
- **Audio Download**: Generated speech can be downloaded as WAV files
- **Temporary File Management**: Automatic cleanup of generated audio files
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Gemini API key from Google AI Studio

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mirellonomikon/izi_tts.git
   cd izi_tts
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   **⚠️ Important**: You need to obtain a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey) and replace `your_gemini_api_key_here` with your actual API key.

4. **Run the application**:
   
   **Option 1 - Using Python**:
   ```bash
   cd src
   streamlit run app.py
   ```
   
   **Option 2 - Using the batch file (Windows)**:
   ```bash
   run_app.bat
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🎯 Usage

1. **Enter Text**: Type or paste the text you want to convert to speech
2. **Select Voice**: Choose from 30 available voices, each with unique characteristics
3. **Choose Model**: Select between Flash (faster) or Pro (higher quality) models
4. **Generate**: Click "🎵 Generate Speech" to create your audio
5. **Listen & Download**: Play the generated audio and download it as a WAV file

## 🎭 Available Voices

The application includes 30 different voices with various characteristics:

| Voice | Style | Voice | Style | Voice | Style |
|-------|-------|-------|-------|-------|-------|
| Zephyr | Bright | Kore | Firm | Orus | Firm |
| Autonoe | Bright | Umbriel | Easy-going | Erinome | Clear |
| Laomedeia | Upbeat | Schedar | Even | Achird | Friendly |
| Sadachbia | Lively | Puck | Upbeat | Fenrir | Excitable |
| Aoede | Breezy | Enceladus | Breathy | Algieba | Smooth |
| Algenib | Gravelly | Achernar | Soft | Gacrux | Mature |
| Zubenelgenubi | Casual | Sadaltager | Knowledgeable | Charon | Informative |
| Leda | Youthful | Callirrhoe | Easy-going | Iapetus | Clear |
| Despina | Smooth | Rasalgethi | Informative | Alnilam | Firm |
| Pulcherrima | Forward | Vindemixtrix | Gentle | Sulafat | Warm |

## 🔧 Configuration

### Streamlit Configuration

The app includes custom Streamlit configuration in `.streamlit/config.toml`:
- Purple theme (`#9c27b0`)
- Dark background
- Custom port (8501)

### Environment Variables

Required environment variables in `.env`:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

## 📁 Project Structure

```
izi_tts/
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── tts_service.py      # Gemini TTS service wrapper
│   ├── ui_components.py    # UI components and styling
│   └── styles.css          # Custom CSS styles
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── .env                    # Environment variables (you need to create this)
├── requirements.txt        # Python dependencies
├── run_app.bat            # Windows batch file to run the app
└── README.md              # This file
```

## 🛠️ Dependencies

- `streamlit` - Web framework for the UI
- `python-dotenv` - Environment variable management
- `google-genai` - Google Gemini AI client

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- UI inspired by modern design principles

---

**🤖 Powered by Gemini AI and Coral ;) • Built with Streamlit**