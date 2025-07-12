import os
import json
from flask import Flask, render_template, request, jsonify
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from config import GITHUB_ENDPOINT, GITHUB_MODEL, GITHUB_TOKEN

app = Flask(__name__)

# GitHub AI API Configuration
endpoint = GITHUB_ENDPOINT
model = GITHUB_MODEL
token = GITHUB_TOKEN

# Initialize the client
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Chat history file
CHAT_HISTORY_FILE = 'chat_history.json'

def load_chat_history():
    """Load chat history from JSON file"""
    try:
        with open(CHAT_HISTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_chat_history(history):
    """Save chat history to JSON file"""
    with open(CHAT_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

@app.route('/')
def index():
    """Main page"""
    chat_history = load_chat_history()
    return render_template('index.html', chat_history=chat_history)

@app.route('/ask', methods=['POST'])
def ask():
    """Handle chat requests"""
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please enter a message'}), 400
        
        # Get response from GitHub AI
        response = client.complete(
            messages=[
                SystemMessage("You are a helpful AI assistant. Provide clear, accurate, and helpful responses."),
                UserMessage(user_message),
            ],
            temperature=0.7,
            top_p=1,
            model=model
        )
        
        bot_response = response.choices[0].message.content
        
        # Save to chat history
        chat_entry = {
            'user': user_message,
            'bot': bot_response,
            'timestamp': str(response.usage.completion_tokens)  # Using completion tokens as timestamp
        }
        
        history = load_chat_history()
        history.append(chat_entry)
        save_chat_history(history)
        
        return jsonify({
            'response': bot_response,
            'history': history
        })
        
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    """Clear all chat history"""
    try:
        save_chat_history([])
        return jsonify({'message': 'Chat history cleared successfully'})
    except Exception as e:
        return jsonify({'error': f'Error clearing history: {str(e)}'}), 500

@app.route('/get_history')
def get_history():
    """Get current chat history"""
    try:
        history = load_chat_history()
        return jsonify({'history': history})
    except Exception as e:
        return jsonify({'error': f'Error loading history: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 