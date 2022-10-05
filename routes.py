#!/usr/bin/env python3.10
# Jesse Hitch - JesseBot@Linux.com
from flask import Flask
from flask import render_template, url_for
import logging as log
import sys
import yaml
# not ready yet
# import personal_app.routes

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


# full path to HTML templates
app = Flask(__name__)


@app.route('/')
def index():
    # Grab site specific information - YAML
    log.info("Good morning, sunshine. It's index time.")
    globals = get_global_variables()
    return render_template('index', globals=globals)


@app.route('/static/images/<filename>')
def images(filename):
    return url_for('static', filename=filename)


@app.route('/static/js/<filename>')
def js(filename):
    return url_for('static', filename=filename)


@app.route('/static/css/<filename>')
def css(filename):
    return url_for('static', filename=filename)
