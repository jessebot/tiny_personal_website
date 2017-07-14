#!/usr/bin/python
# Code by JesseBot@Linux.com
# 2/11/16
# Production web routing bottle file

import bottle
from bottle import redirect, request, response, route
from bottle import run, static_file, template
import logging as log
import os
import sys
import yaml


def get_global_variable(global_variable):
    """ gets global variable given string variable name"""
    with open('./config/config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"][global_variable]
    return txt


# set logging
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
# Grab site specific information
WEB_ROOT = get_global_variable('web_root')
# full path to HTML templates
bottle.TEMPLATE_PATH.insert(0,
                            '{0}/front_end/views/'.format(WEB_ROOT))


@route('/')
def index():
    favicon = get_global_variable('favicon')
    browser_tab_title = get_global_variable('website_title')
    main_pic = get_global_variable('profile_image')
    name = get_global_variable('profile_name')
    header_quotation = get_global_variable('profile_quote')
    blurb = get_global_variable('profile_blurb')
    github_URL = get_global_variable('github_URL')
    linkedin_URL = get_global_variable('linkedin_URL')
    gdoc_URL = get_global_variable('resume_google_doc')
    resume_pdf_download_URL = get_global_variable('resume_pdf_download')
    resume_docx_download_URL = get_global_variable('resume_docx_download')
    try:
        fork_me = get_global_variable('fork_me')
    except:
        fork_me = None
    optional_panel = get_global_variable('optional_panel')
    optional_panel_title = get_global_variable('opt_panel_title')
    optional_panel_pic = get_global_variable('opt_panel_image')
    optional_panel_button_text = get_global_variable('opt_panel_button_text')
    optional_panel_button_URL = get_global_variable('opt_panel_URL')
    return template('index', favicon=favicon,
                    browser_tab_title=browser_tab_title, main_pic=main_pic,
                    name=name, header_quotation=header_quotation,
                    github_URL=github_URL, linkedin_URL=linkedin_URL,
                    gdoc_URL=gdoc_URL,
                    resume_pdf_download_URL=resume_pdf_download_URL,
                    resume_docx_download_URL=resume_docx_download_URL,
                    fork_me=fork_me, optional_panel=optional_panel,
                    optional_panel_title=optional_panel_title,
                    optional_panel_pic=optional_panel_pic, blurb=blurb,
                    optional_panel_button_text=optional_panel_button_text,
                    optional_panel_button_URL=optional_panel_button_URL)


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='{0}/front_end/images'.format(WEB_ROOT))


@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='{0}/front_end/js'.format(WEB_ROOT))


@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='{0}/front_end/css'.format(WEB_ROOT))

@route('/fonts/<filename>')
def fonts(filename):
    return static_file(filename, root='{0}/front_end/fonts'.format(WEB_ROOT))

@route('/love')
def love():
    favicon = get_global_variable('favicon')
    return template('love', favicon=favicon)

@route('/hate')
def hate():
    favicon = get_global_variable('favicon')
    return template('hate', favicon=favicon)
