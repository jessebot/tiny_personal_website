# Author: Jesse Hitch - JesseBot@Linux.com
# LICENSE: AGPL

from flask import Flask
from flask import render_template
import logging as log
from os import environ as env
from os import path
import sys
import yaml

PWD = path.dirname(__file__)
# get config file location from env vars
CONFIG_FILE = env.get("CONFIG_FILE", f"{PWD}/config/config.yaml")

# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("tiny personal website logging config loaded")


def get_config_variables() -> dict:
    """
    Gets config.yaml variables from YAML file. Returns dict.
    """
    with open(CONFIG_FILE, 'r') as yml_file:
        doc = yaml.safe_load(yml_file)
    return doc

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    """
    single page resume site with downloadable PDF for resume
    """
    # Grab site specific information - YAML
    log.info("Good morning, sunshine. It's index time.")
    config_vars = get_config_variables()
    social_links = config_vars['social_links']
    return render_template('index.html',
                           config_vars=config_vars,
                           social_links=social_links)
