# Tiny Personal Website [![AGPL license](https://img.shields.io/badge/License-AGPL-blue.svg)](./LICENSE)

This is a small Python based personal website aimed first and foremost at being a resume.
I originally wrote this a decade or so ago, and recently absolutely borked my
react website, resulting in me quickly resurrecting this thing in about a day
and a half. It was actually pretty fun though, so I've continued to add little features.
This one does the same thing, but better, and faster, with less js.
Feel free to fork this and make it your own, but keep it open source.

[![made-with-docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![made-with-python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![made-wth-flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.2.x/)
[![made-with-bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

<img src="./example.png" alt="screenshot of jessebot.work which serves as an example website. It features a picture of Jesse a person with blue hair that is 31. There is a blurb about them that you can read in tiny_personal_website/config/config.yaml and link icons to github, gitlab, and linkedin." style="width: 40%;" align="left">

## Getting Started

Clone this github repo into your desired webroot, and install dependencies with [poetry](https://python-poetry.org/docs/#installation):

`poetry install`

You can configure everything (e.g. website title, your photo, quote, etc)
by editing `tiny_personal_website/config/config.yaml` and replacing all the Jesse data with your own.

For testing locally with docker, you can do:

```bash
docker build . -t <name of tag you want>

# to test locally, you can do -p 8000:8080 to forward
# port 8080 on the container to port 8000 on your local machine
docker run --rm -p 8000:8080 <name of the tag you used>
```

Then you can go to http://127.0.0.1:8000 in a browser to view your changes.

### Deploying on an app platform

You want the following command plugged into where-ever this runs
(e.g. digital ocean app platform):

```bash
gunicorn --worker-tmp-dir /dev/shm app:app
```

And the container port of note is port 8080.
