from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! This is my Flask application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
