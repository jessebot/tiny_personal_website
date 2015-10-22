# production jessebot.com python file

import logging 
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import sys
import yaml

stream = open(config.yaml)
WEB_ROOT = ""

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

logging.info("logging config loaded")

@route('/')
def index():
    return template('index')

@route('/contact')
def contact():
    return template('contact')

@route('/about')
def about():
    return template('about')

@route('/legacy')
def legacy():
    redirect ("http://legacy.jessebot.com")

@route('/hate')
def hate():
    return template('hate')

@route('/photo')
@route('/photo/')
def photo():
    redirect('http://photo.jessebot.com')

@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='WEB_ROOT/{0}'.format(images))

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='WEB_ROOT/{0}'.format(js))

@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='WEB_ROOT/{0}'.format(css))
