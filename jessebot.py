# production jessebot.com python file

from lib import get_global_variable
import logging
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import sys
import yaml

WEB_ROOT = get_global_variable('web_root')

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
    redirect("http://legacy.jessebot.com")


@route('/hate')
def hate():
    return template('hate')


@route('/photo')
@route('/photo/')
def photo():
    redirect('http://photo.jessebot.com')


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='{0}/images'.format(WEB_ROOT))


@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='{0}/js'.format(WEB_ROOT))


@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='{0}/css'.format(WEB_ROOT))
