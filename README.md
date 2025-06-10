# AI Chat with Voice

A real-time chat application that uses OpenAI's GPT model for text generation and text-to-speech capabilities. The application provides a WebSocket-based streaming interface for interactive conversations with voice synthesis.

## Features

- Real-time chat interface using WebSocket
- Integration with OpenAI's GPT model for natural language processing
- Text-to-speech synthesis of AI responses
- Automatic reconnection handling
- Modern, responsive UI

## API Endpoints

- `GET /` - Redirects to the chat interface
- `GET /static/index.html` - The main chat interface
- `WebSocket /api/chat/stream` - WebSocket endpoint for streaming chat and voice responses

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Start the server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
.
├── core/
│   ├── config/
│   │   └── settings.py
│   ├── llm/
│   │   └── service.py
│   ├── tts/
│   │   └── service.py
│   └── websocket/
│       ├── manager.py
│       └── router.py
├── static/
│   └── index.html
├── tests/
│   ├── unit/
│   │   ├── test_llm_service.py
│   │   └── test_tts_service.py
│   └── system/
│       └── test_websocket.py
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Testing

Run the test suite:
```bash
pytest tests/ -v --cov=core
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 