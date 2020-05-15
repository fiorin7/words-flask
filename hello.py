import subprocess
import ruamel.yaml as yaml
from flask import Flask

with open("config.yaml") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search/<word>')
def get_name(word):
    p = subprocess.Popen([config['words']['bin']], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd = config['words']['cwd'])
    out, err = p.communicate(word.encode())
    return '<pre>' + out.decode() + '</pre>'


if __name__ == '__main__':
    app.run()
