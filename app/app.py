import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read environment variables or use default values
port = int(os.environ.get('APP_PORT', 5000))
message = os.environ.get('MESSAGE', 'Hello, World!')

@app.route('/')
def get_message():
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=port)

