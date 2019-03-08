#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import os
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# Customiziable

project = 'STAT 157, Spring 19'
copyright = '2018--2019, Contributors'
author = "All contributors"

html_theme_options = {
    'header_links' : [
        # The items in the navbar under the title, the format is
        # Name, Link, (keep True, ignore its meaning), font-awesome icon name (can be empty).
        # You can search all icons at https://fontawesome.com/icons?d=gallery
        ('Textbook', 'https://en.diveintodeeplearning.org/', True, 'fas fa-book'),
        ('Video', 'https://www.youtube.com/playlist?list=PLZSO_6-bSqHQHBCoGaObUljoXAyyqhpFW', True, 'fas fa-video'),
        ('Forum', 'https://discuss.mxnet.io/c/courses', True, 'fas fa-user-tie'),
        ('Github', 'https://github.com/diveintodeeplearning/berkeley-stat-157', True, 'fab fa-github'),
    ],
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'show_footer': False,
}

# ========== you often don't need to change the rest ========
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    # 'nbsphinx',
    # 'IPython.sphinxext.ipython_console_highlighting',
]
master_doc = 'index'
source_parsers = {'.md': CommonMarkParser}
source_suffix = ['.rst', '.ipynb', '.md']
version = ''
release = ''
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'mx-theme', '**.ipynb_checkpoints']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme_path = ['../mx-theme']
html_theme = 'mxtheme'
html_favicon = '_static/gluon_s2.png'
html_static_path = ['_static']
html_search_language = 'en'
htmlhelp_basename = 'DiveIntoDeepLearning'
# notebooks will be executed by sphnix_plugin
nbsphinx_execute = 'never'
# let the source file format to be xxx.ipynb instead of xxx.ipynb.txt
html_sourcelink_suffix = ''

def setup(app):
    app.add_transform(AutoStructify)
    app.add_javascript('google_analytics.js')
    app.add_config_value('recommonmark_config', {
    }, True)
