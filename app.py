from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello CI/CD working successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello CI/CD working successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
