import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search/<word>')
def get_name(word):
    p = subprocess.Popen(['bin/words'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd = '/home/matus/sources/whitakers-words')
    out, err = p.communicate(word.encode())
    return '<pre>' + out.decode() + '</pre>'


if __name__ == '__main__':
    app.run()
