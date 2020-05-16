import subprocess
import ruamel.yaml as yaml
import re
from flask import Flask
from flask import render_template
from flask import request, redirect
from unidecode import unidecode

with open("config.yaml") as stream:
    try:
        config = yaml.safe_load(stream)
        print(config)
    except yaml.YAMLError as exc:
        print(exc)

# LEMMAS ######################################################################
with open("lemmas_doc2.txt", "rt", encoding="utf-8") as dict_file:
    dict_file = dict_file.readlines()

dict_dict = {}
lemmas = []

for entry in dict_file:
    if entry and entry[0].isdigit():
        entry = entry[3:]
    entry_split = re.split(", | |,|\n", entry)
    no_diacritics_lemma = unidecode(entry_split[0]).replace('-', '')
    if no_diacritics_lemma != '':
        dict_dict.setdefault(no_diacritics_lemma, [])
        if no_diacritics_lemma not in lemmas:
            lemmas.append(no_diacritics_lemma)
        dict_dict[no_diacritics_lemma].append(entry)

################################################################################

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/search')

def get_examples(form):
    pass
def get_lemma():
    word = request.args.get('word')
    if not word:
        word = 'Нищо-не-си-написал-ей'
    p = subprocess.Popen([config['words']['bin']], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd = config['words']['cwd'])
    out, err = p.communicate(word.encode())
    full_result = out.decode()
    print(full_result)

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
    print(only_latin)

    pattern = r"^.*?\[\w*\]"
    matches = re.findall(pattern, only_latin, re.MULTILINE)
    print(matches)
    no_pattern_matches = []
    
    for match in matches:
        excess = re.findall(r'\s+\[\w+\]', match)
        excess = excess[0]
        match = match.replace(excess, '')
        no_pattern_matches.append(match)
    print(no_pattern_matches)
    no_pattern_dict = {}

    for match in no_pattern_matches:
        split_match = re.split(r', | ', match)
        if split_match[0]:
            no_pattern_dict[match] = split_match[0]

    

    return render_template("search.html", no_pattern_dict=no_pattern_dict, word=word)



@app.route('/entry/<word>')
def get_entry(word):
    if word in lemmas:
        entries = dict_dict[word]
    else:
        entries = ['Думата или не е в малкия речник, или нещо пречи да я намеря. :(']
    return render_template("lemma-entry.html", entries=entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
