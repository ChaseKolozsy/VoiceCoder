from flask import Flask, request, jsonify
from VoiceControlledCodingEnvironment import VoiceControlledCodingEnvironment

app = Flask(__name__)
vcce = VoiceControlledCodingEnvironment()

@app.route('/translate', methods=['POST'])
def translate_command():
    data = request.json
    translation = vcce.translate_command(data['command'], data['target_syntax'])
    return jsonify({"translation": translation})

@app.route('/speak', methods=['POST'])
def speak_text():
    vcce.speak(request.json['text'])
    return jsonify({"message": "Text spoken successfully"})

@app.route('/listen', methods=['GET'])
def listen_command():
    command = vcce.listen()
    return jsonify({"command": command})

# Add similar routes for other VCCE methods

if __name__ == '__main__':
    app.run(port=your_chosen_port)