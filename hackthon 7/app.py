from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to handle requests from different origins

@app.route('/')
def index():
    # Render the main HTML page
    return render_template('index.html')

@app.route('/api/assist', methods=['POST'])
def assist_user():
    # Mock AI assistance function, can later be integrated with real AI APIs
    user_input = request.json.get('input')
    response = {"message": f"Received and processed your input: {user_input}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
