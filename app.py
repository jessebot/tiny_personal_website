#!/usr/bin/env python3.10
# Jesse Hitch - JesseBot@Linux.com
from flask import Flask
from flask import render_template
import logging as log
import sys
import yaml

# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")


def get_global_variables():
    """
    Gets global variables from YAML file. Returns dict.
    """
    with open('./config/config.yaml', 'r') as yml_file:
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
    globals = get_global_variables()
    return render_template('index.html', globals=globals)
