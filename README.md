# Dict Proto

Prototype of a digital Latin-Bulgarian dictionary with morphological analysis.

The app presents a simple search interface. Upon entering a form of a Latin word it's analyzed by Whitaker's Words. The output of this analysis is used to determine the possible lemmas which are then retrieved from the dictionary database.

The database of this prototype includes a limited number of Latin lemmas and their Bulgarian meanings.

A list of all mentions of the form in the database is also generated.


# Installation

We use [Whitaker's Words](https://mk270.github.io/whitakers-words/) for the morphological analysis. To use this project you need to have it installed on your system. Follow the instructions in the Whitaker's Words repository.

Install [pipenv](https://github.com/pypa/pipenv).  Then clone the
project and in the project directory run

``` shell
pipenv install
```

to install dependencies and enter the virtualenv shell.

# Usage

Configure paths for the `words` binary from Whitaker's Words in `config.yaml`.  Copy the example configuration file to your own personal config (**do not put this personal config in git**).  The copy is where you write your personal configuration.

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

# Building and deploying

To build the docker image, you must first build [Whitaker's
Words](https://mk270.github.io/whitakers-words/) for linux.

Clone the words project into `./words` directory in this project then
follow their build instructions.

When this is done, run

``` shell
docker-compose build
```

to build the image.
