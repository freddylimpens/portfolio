#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'contact@limpica.net'
SITENAME = u'Limpica.net'
SITEURL = '/staging'
SITESUBTITLE = 'CéCiLe Picard & FredDY Limpens works and ideas'

PATH = 'content'
STATIC_PATHS = ['media']
OUTPUT_PATH = 'output/staging'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

DISPLAY_HOME = False
MENU_INTERNAL_PAGES = (
    ('Projects', 'category/projects.html', 'category/projects.html'),
    ('Notes', 'category/notes.html', 'category/notes.html'),
    ('CCL', 'author/ccl.html', 'author/ccl.html'),
    ('FDY', 'author/fdy.html', 'author/fdy.html'),
)
MENUITEMS = (
    # ('CV', 'http://limpica.net/fdy/cv'),
)
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
        #   ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = "/home/freddy/src/pelican-themes/simple-bootstrap"
# THEME = "/home/freddy/src/pelican-themes/photowall"
# THEME = "/home/freddy/src/blue-penguin"
THEME = "/home/freddy/src/minimalist-portfolio"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.attr_list': {},
    },
    'output_format': 'html5',
}
