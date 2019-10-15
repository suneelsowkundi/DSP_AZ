from flask import Flask

app = Flask(__name__)


@app.route('/basic')
def hello():
    word = 'Hello World !!'
    return word

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021, debug=True)
