#!/usr/bin/python
# production web routing bottle file

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


# Grab site specific information
WEB_ROOT = get_global_variable('web_root')
# set logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.info("logging config loaded")
# full path to HTML templates
bottle.TEMPLATE_PATH.insert(0,
                            '{0}/front_end/html_templates/'.format(WEB_ROOT))


@route('/')
def index():
    favicon = get_global_variable('favicon')
    browser_tab_title = get_global_variable('website_title')
    main_pic = get_global_variable('profile_image')
    name = get_global_variable('profile_name')
    header_quotation = get_global_variable('profile_quote')
    GitHub_URL = get_global_variable('github_URL')
    gdoc_URL = get_global_variable('resume_google_doc')
    resume_pdf_download_URL = get_global_variable('resume_pdf_download')
    resume_docx_download_URL = get_global_variable('resume_docx_download')
    optional_panel = get_global_variable('optional_panel')
    optional_panel_title = get_global_variable('optional_panel_title')
    optional_panel_pic = get_global_variable('optional_panel_image')
    optional_panel_button_text = get_global_variable('optional_panel_link_title')
    optional_panel_button_URL = get_global_variable('optional_panel_URL')
    return template('index', favicon=favicon, tab_title=tab_title,
                    main_pic=main_pic, name=name, header_quotation=header_quotation,
                    GitHub_URL=GitHub_URL, gdoc_URL=gdoc_URL,
                    resume_pdf_download_URL=resume_pdf_download_URL,
                    resume_docx_download_URL=resume_docx_download_URL,
                    optional_panel_title=optional_panel_title,
                    optional_panel_pic=optional_panel_pic,
                    optional_panel_button_text=optional_panel_button_text,
                    optional_panel_button_URL=optional_panel_button_URL)


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
