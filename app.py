#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)###
#----------------------------------------
#from flask import Flask, render_template

#app = Flask(__name__, template_folder='.')
#app = Flask(__name__)


#@app.route('/')
#def index():
#   return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)'''
#----------------------------------------  
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Configure Gemini with your API key
client = genai.Client()

chatClient = client.chats.create(model="gemini-2.5-flash")
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = chatClient.send_message(prompt)

        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

    
    
