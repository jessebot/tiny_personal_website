#!/usr/bin/python
# Jesse Hitch - JesseBot@Linux.com
# 1/10/19 Production Web Routing File -- Personal Routes
import bottle
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import logging as log
import os
import sys
import yaml
import band_names_db


def get_global_variables():
    """
    Gets global variables from YAML file. Returns dict.
    """
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"]
    return txt


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


# Web routes below this line...
# full path to HTML templates
WEB_ROOT = get_global_variables()['web_root']
bottle.TEMPLATE_PATH.insert(0, '{0}/views/'.format(WEB_ROOT))


@route('/google1ab5c73d1f31729d.html')
def goog():
    # allow google to crawl me harder
    return static_file('google1ab5c73d1f31729d.html', root=WEB_ROOT+'/views/')


@route('/next-band')
def next_band():
    log.info("oh hi, you must be here to see the name of my next band")
    # Grab site specific information - YAML
    globals = get_global_variables()

    all_bands = band_names_db.get_all_bands()
    log.info("received band.db response: {0}".format(all_bands))

    return template('next-band', globals=globals, bands=all_bands)


@route('/next-band', method='POST')
def next_band_submit():
    # get band from post
    inputBand = request.forms.get('inputBand')
    log.info("received band name: {0}".format(inputBand))

    # add new band to db
    add_new_band = band_names_db.add_new_band(inputBand)

    # if success redirect back to main page
    if add_new_band == "Success":
        redirect("/next-band")
    else:
        return "<p>THERE WAS AN ERROR: {0}</p>".format(add_new_band)


@route('/love')
def love():
    # Grab site specific information - YAML
    globals = get_global_variables()
    likes = get_ld_variables("likes")
    sorted_likes = sorted_vars(likes)
    return template('love', globals=globals, likes=sorted_likes)


@route('/hate')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    dislikes = get_ld_variables("dislikes")
    sorted_dislikes = sorted_vars(dislikes)
    return template('hate', globals=globals, dislikes=sorted_dislikes)


@route('/resources')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    dislikes = get_ld_variables("dislikes")
    sorted_dislikes = sorted_vars(dislikes)
    return template('hate', globals=globals, dislikes=sorted_dislikes)


@route('/nutrition')
def nutrition():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('nutrition', globals=globals)


@route('/trans')
def trans():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('trans', globals=globals)


@route('/tech')
def tech():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('tech', globals=globals)


@route('/resources')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    dislikes = get_ld_variables("dislikes")
    sorted_dislikes = sorted_vars(dislikes)
    return template('resources', globals=globals, dislikes=sorted_dislikes)


@route('/dev')
def dev():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('dev', globals=globals)
