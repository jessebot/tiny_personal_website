#!/usr/bin/python
# Code by Jesse Hitch - JesseBot@Linux.com
# 7/15/17
# Production Web Routing File

import bottle
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import logging as log
import os
import sys
import yaml


def get_global_variables():
    """ gets global variable given string variable name"""
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"]
    return txt


def get_web_root():
    """ gets global variable given string variable name"""
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"]['web_root']
    return txt


# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
# Grab site specific information -YAML
WEB_ROOT = get_web_root()
# full path to HTML templates
bottle.TEMPLATE_PATH.insert(0,
                            '{0}/views/'.format(WEB_ROOT))


@route('/')
def index():
    # Grab site specific information - YAML
    log.info("oh hi, this is the route?")
    globals = get_global_variables()
    return template('index', globals=globals)


@route('/robots.txt')
def index():
    return static_file('robots.txt', root='{0}'.format(WEB_ROOT))


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='{0}/images'.format(WEB_ROOT))


@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='{0}/css'.format(WEB_ROOT))


@route('/fonts/<filename>')
def fonts(filename):
    return static_file(filename, root='{0}/fonts'.format(WEB_ROOT))


@route('/love')
def love():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('love', globals=globals)


@route('/hate')
def hate():
    # Grab site specific information - YAML
    globals = get_global_variables()
    return template('hate', globals=globals)
