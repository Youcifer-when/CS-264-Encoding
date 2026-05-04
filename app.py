from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import caeesar
import vigenere
import morsecode
app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/history')
def history_page():
    return render_template('history.html')

@app.route('/process', methods=['POST'])
def process_cipher():
    # Catch the package from JS
    data = request.json 
    
    # Extract the info
    user_msg = data.get('message', '').lower()
    user_key = data.get('key', '').lower()
    selected_cipher = data.get('cipher', 'caesar')
    action_type = data.get('action', 'encode') 
    
    result = "Error handling cipher."

    # Route the data to the correct function file
    if selected_cipher == 'caesar':
        try:
            shift = int(user_key)
        except ValueError:
            shift = 0 # Fallback if they somehow bypassed the number input
        result = caeesar.caesar(user_msg, shift, action_type)
        
    elif selected_cipher == 'vigenere':
        result = vigenere.vigenere(user_msg, user_key, action_type)
        
    elif selected_cipher == 'morse':
        # Morse has different functions for encoding vs decoding
        if action_type == 'encode':
            result = morsecode.words_to_morse(user_msg)
        elif action_type == 'decode':
            result = morsecode.morse_to_words(user_msg)
            
    # Send the final string back to the webpage
    return jsonify({'result': result}) 

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

if __name__ == '__main__':
    app.run(debug=True)

