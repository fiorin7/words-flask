# words-flask

Run [Whitakers Words](https://mk270.github.io/whitakers-words/)
through [Flask](https://flask.palletsprojects.com/en/1.1.x/).

# Installation

Install [pipenv](https://github.com/pypa/pipenv).  Then clone the
project and in the project directory run

``` shell
pipenv install
pipenv shell
```

to install dependencies and enter the virtualenv shell.

# Usage

Configure paths for the words binary in `config.yaml`.

``` shell
cp config.example.yaml config.yaml
```

Open this file and update the paths.  `words.cwd` is the path to the
directory where the data files are located (the main directory of
words).  `words.bin` is the binary, for example `words.exe` *relative*
to the `words.cwd` directory.

Then run

``` shell
python hello.py
```

to start the flask server.
