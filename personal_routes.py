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


# full path to HTML templates
WEB_ROOT = get_global_variables()['web_root']
bottle.TEMPLATE_PATH.insert(0, '{0}/views/'.format(WEB_ROOT))

@route('/next-band')
def dev():
    # Grab site specific information - YAML
    log.info("oh hi, you must be here to see the name of my next band")
    globals = get_global_variables()
    return template('next_band', globals=globals)
