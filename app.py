from flask import Flask

app = Flask(__name__)


@app.route('/basic')
def hello():
    word = 'Hello WORLD !!'
    return word

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
