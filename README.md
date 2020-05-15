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

<<<<<<< HEAD
Copy config.example.yaml. The copy is where you write your personal configurations.
Open this file and update the paths.  `words.cwd` is the path to the
directory where the data files are located (the main directory of
words).  `words.bin` is the binary, for example `words.exe` *relative*
to the `words.cwd` directory.
=======
Open `config.yaml` file and update the paths.  `words.cwd` is the path
to the directory where the data files are located (the main directory
of words).  `words.bin` is the binary, for example `words.exe`.  On
windows you might need to specify full path to the executable file.
>>>>>>> origin/feature/update-run-instructions

Then run

``` shell
pipenv run python hello.py
```

to start the flask server.

# Building and deploying

To build the docker image, you must first build [Whitakers
Words](https://mk270.github.io/whitakers-words/) for linux.

Clone the words project into `./words` directory in this project then
return their build instructions.

When this is done, run

``` shell
docker-compose build
```

to build the image.

Then run

``` shell
docker-compose push
```

to push the new version to Google Cloud platform.

[Update the
image](https://console.cloud.google.com/run/deploy/europe-west1/words-flask?project=words-flask)
used by the google service to your latest version and redeploy.
