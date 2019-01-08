#!/usr/bin/python
# Jesse Hitch - JesseBot@Linux.com
# 7/15/18 Production Web Routing File
import bottle
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import logging as log
import os
import sys
import yaml
import personal_routes


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
def nextband():
    # Grab site specific information - YAML
    log.info("oh hi, you must be here to see the name of my next band")
    globals = get_global_variables()
    return template('next-band', globals=globals)


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

