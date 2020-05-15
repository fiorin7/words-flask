import subprocess
import ruamel.yaml as yaml
import re
from flask import Flask
from flask import render_template
from flask import request, redirect

with open("config.yaml") as stream:
    try:
        config = yaml.safe_load(stream)
        print(config)
    except yaml.YAMLError as exc:
        print(exc)


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    background_image_url = "url_for('static', filename='header-dict.py')"
    return render_template("index.html", background_image_url=background_image_url)

def get_form():
    if request.method == "POST":
        req = request.form
        print(req)

    return redirect(request.url)


@app.route('/search')
def get_lemma():
    word = request.args.get('word')
    p = subprocess.Popen([config['words']['bin']], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd = config['words']['cwd'])
    out, err = p.communicate(word.encode())
    full_result = out.decode()

    only_latin = ''
    start_idx = None
    for i in range(len(full_result)):
        if full_result[i] == '=' and full_result[i+1] == '>':
            start_idx = i+2
            break
    only_latin = full_result[start_idx:-1]
    for i in range(len(only_latin)):
        if only_latin[i] == '=' and only_latin[i+1] == '>':
            end_idx = i
            break
    only_latin = only_latin[:end_idx]

    pattern = r"^.*?\[\w*\]"
    matches = re.findall(pattern, only_latin, re.MULTILINE)
    no_pattern_matches = []
    
    for match in matches:
        excess = re.findall(r'\s+\[\w+\]', match)
        excess = excess[0]
        match = match.replace(excess, '')
        no_pattern_matches.append(match)




    return render_template("search.html", cleared_matches=no_pattern_matches, word=word)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
