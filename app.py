from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000')