#!/usr/bin/python
# production jessebot.com web routing bottle file

import bottle
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import logging
import sys
import yaml


def get_global_variable(global_variable):
    """ gets global variable given string variable name"""
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"][global_variable]
    return txt


# grab web root
WEB_ROOT = get_global_variable('web_root')
# set logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.info("logging config loaded")
# full path to HTML templates
bottle.TEMPLATE_PATH.insert(0,
                            '{0}/front_end/html_templates/'.format(WEB_ROOT))


@route('/')
def index():
    return template('index')


@route('/hate')
def hate():
    return template('hate')


@route('/photo')
@route('/photo/')
def photo():
    redirect('http://photo.jessebot.com')


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='{0}/front_end/images'.format(WEB_ROOT))


@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='{0}/front_end/js'.format(WEB_ROOT))


@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='{0}/front_end/css'.format(WEB_ROOT))
