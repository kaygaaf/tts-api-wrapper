from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', 'demo-key')
AFFILIATE_LINK = "https://try.elevenlabs.io/6rf9nw0kbn9x"

@app.route('/')
def home():
    return render_template('index.html', affiliate_link=AFFILIATE_LINK)

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    voice_id = data.get('voice_id', '21m00Tcm4TlvDq8ikWAM')
    
    # In production, this calls ElevenLabs API
    # For demo, return mock response
    return jsonify({
        'status': 'success',
        'audio_url': f'/demo-audio/{voice_id}',
        'characters_used': len(text),
        'upgrade_link': AFFILIATE_LINK
    })

@app.route('/api/voices')
def list_voices():
    return jsonify({
        'voices': [
            {'id': '21m00Tcm4TlvDq8ikWAM', 'name': 'Rachel', 'preview': '/preview/rachel'},
            {'id': 'AZnzlk1XvdvUeBnXmlld', 'name': 'Domi', 'preview': '/preview/domi'},
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
