# 🤖 AI Chatbot

A modern, responsive chatbot web application built with Python Flask and GitHub AI inference API (GPT-4.1).

## ✨ Features

- **Real-time Chat**: Interactive chat interface with instant responses
- **Chat History**: Persistent storage of all conversations in JSON format
- **Modern UI**: Clean, responsive design with smooth animations
- **Easy Controls**: Start new chat sessions and clear history
- **Loading States**: Visual feedback during AI processing
- **Mobile Responsive**: Works perfectly on all devices

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **AI Model**: GitHub AI Inference API (GPT-4.1)
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: Local JSON file
- **Styling**: Modern CSS with gradients and animations

## 📁 Project Structure

```
chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── sample.py             # Original sample code
├── prd.md               # Product Requirements Document
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   └── style.css        # CSS styling
└── chat_history.json    # Chat storage (created automatically)
```

## 🚀 Quick Start

### 1. Install Dependencies

Make sure you're in your `chatbot` conda environment:

```bash
conda activate chatbot
pip install -r requirements.txt
```

### 2. Environment Setup

Create a `.env` file in the project root with your GitHub AI credentials:

```env
GITHUB_ENDPOINT=https://models.github.ai/inference
GITHUB_MODEL=openai/gpt-4.1
GITHUB_TOKEN=your_github_token_here
```

### 3. Run the Application

```bash
python app.py
```

### 4. Access the Chatbot

Open your browser and go to: `http://localhost:5000`

## 🎯 Usage

1. **Start Chatting**: Type your message and press Enter or click Send
2. **View History**: All conversations are automatically saved and displayed
3. **New Chat**: Click "Start New Chat" to clear the current session
4. **Clear History**: Click "Clear History" to delete all saved conversations

## 🔧 Configuration

### Environment Variables

- `GITHUB_ENDPOINT`: GitHub AI inference endpoint
- `GITHUB_MODEL`: AI model to use (default: openai/gpt-4.1)
- `GITHUB_TOKEN`: Your GitHub personal access token

### Customization

- **Model**: Change the model in `.env` file
- **Styling**: Modify `static/style.css` for custom themes
- **System Prompt**: Edit the system message in `app.py`

## 📱 Features

### Chat Interface
- Real-time message exchange
- Loading animations
- Error handling
- Responsive design

### History Management
- Automatic chat saving
- JSON-based storage
- History clearing
- Session management

### UI/UX
- Modern gradient design
- Smooth animations
- Mobile-friendly layout
- Intuitive controls

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're in the correct conda environment
   ```bash
   conda activate chatbot
   pip install -r requirements.txt
   ```

2. **API Errors**: Check your GitHub token in the `.env` file
   - Ensure the token has the correct permissions
   - Verify the endpoint URL is correct

3. **Port Issues**: If port 5000 is busy, change it in `app.py`
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
   ```

## 📝 API Endpoints

- `GET /`: Main chat interface
- `POST /ask`: Send message to AI
- `POST /clear_history`: Clear all chat history
- `GET /get_history`: Retrieve chat history

## 🔒 Security Notes

- Keep your GitHub token secure
- Don't commit `.env` file to version control
- The application runs locally by default

## 🚀 Future Enhancements

- User authentication
- Multiple chat sessions
- File upload support
- Voice input/output
- Custom AI models
- Database integration

## 📄 License

This project is for educational purposes. Feel free to modify and use as needed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Happy Chatting! 🤖✨** 