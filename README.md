# words-flask

Run [Whitakers Words](https://mk270.github.io/whitakers-words/)
through [Flask](https://flask.palletsprojects.com/en/1.1.x/).

# Installation

Install [pipenv](https://github.com/pypa/pipenv).  Then clone the
project and in the project directory run

``` shell
pipenv install
```

to install dependencies and enter the virtualenv shell.

# Usage

Configure paths for the words binary in `config.yaml`.  Copy the
example configuration to your own personal config (**do not put this
personal config in git**):

``` shell
cp config.example.yaml config.yaml
```

Open `config.yaml` file and update the paths.  `words.cwd` is the path
to the directory where the data files are located (the main directory
of words).  `words.bin` is the binary, for example `words.exe`.  On
windows you might need to specify full path to the executable file.

Then run

``` shell
pipenv run python hello.py
```

to start the flask server.
