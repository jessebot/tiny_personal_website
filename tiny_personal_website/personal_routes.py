#!/usr/bin/env python3.10
# JesseBot@Linux.com
# last update 2022-10-07 17:06:07.0 +0200
from flask import Flask
from flask import render_template
import logging as log
import sys
import yaml

# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
# flask app init
app = Flask(__name__, static_folder='static')


def get_config_variables():
    """
    Gets config.yaml variables from YAML file. Returns dict.
    """
    with open('./config/config.yaml', 'r') as yml_file:
        doc = yaml.safe_load(yml_file)
    return doc


def get_ld_variables(ld_var):
    """
    Gets global variables from YAML file. Returns dict.
    """
    with open('./config/config_likes_dislikes.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc[ld_var]
    return txt


def sorted_vars(some_dict):
    """
    Iterates through a dict and fixes list values to be alphabitized
    takes a dict.
    """
    for key, value in some_dict.items():
        value.sort()
        some_dict[key] = value
    return some_dict


@app.route('/like')
def love():
    # Grab site specific information - YAML
    globals = get_global_variables()
    likes = get_ld_variables("likes")
    sorted_likes = sorted_vars(likes)
    return render_template('like', config_vars=config_vars, likes=sorted_likes)


@app.route('/dislike')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    dislikes = get_ld_variables("dislikes")
    sorted_dislikes = sorted_vars(dislikes)
    return render_template('dislike', config_vars=config_vars,
                           dislikes=sorted_dislikes)


@app.route('/health')
def nutrition():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return render_template('health', config_vars=config_vars)


@app.route('/health/nutrition')
def nutrition():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return render_template('nutrition', config_vars=config_vars)


@app.route('/health/trans')
def trans():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return render_template('trans', config_vars=config_vars)


@app.route('/tech')
def tech():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return render_template('tech', config_vars=config_vars)


@app.route('/resources')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    dislikes = get_ld_variables("dislikes")
    sorted_dislikes = sorted_vars(dislikes)
    return render_template('resources', config_vars=config_vars)
