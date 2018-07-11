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

# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")


def get_global_variables():
    """
    Gets global variables from YAML file. Returns dict.
    """
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"]
    return txt


# full path to HTML templates
WEB_ROOT = get_global_variables()['web_root']
bottle.TEMPLATE_PATH.insert(0, '{0}/views/'.format(WEB_ROOT))


@route('/')
def index():
    # Grab site specific information - YAML
    log.info("Good morning, sunshine. It's index time.")
    globals = get_global_variables()
    return template('index', globals=globals)


@route('/robots.txt')
def robots():
    return static_file('robots.txt', root=WEB_ROOT+'')


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root=WEB_ROOT+'/images')


@route('/js/<filename>')
def js(filename):
    return static_file(filename, root=WEB_ROOT+'/js')


@route('/css/<filename>')
def css(filename):
    return static_file(filename, root=WEB_ROOT+'/css')


@route('/fonts/<filename>')
def fonts(filename):
    return static_file(filename, root=WEB_ROOT+'/fonts')
