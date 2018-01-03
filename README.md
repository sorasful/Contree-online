# Contrée Online

This is a web application for hosting and playing games of [Contrée](https://fr.wikipedia.org/wiki/Belote_contr%C3%A9e).

It is written in Python.

## Compiling

Trick question: Python is not compiled

## Testing

Run `tox` to execute all tests.

## Packaging

Run `docker build -t sorasful/contree` to build a Docker image

## Running

In order to run locally, install requirements (maybe in a virtual environment) and run main module.

```
pip3 install -rrequirements.txt
python3 main.py
```

In order to run using Docker, after building the Docker image, run it.

```
docker run -d --name contree -p5000:5000 sorasful/contree
```

You will be able to access the application at http://localhost:5000/.
