#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'fdy@limpica.net'
SITENAME = u'Fdy Projects'
SITEURL = '/fdy'

PATH = 'content'
STATIC_PATHS = ['media']
OUTPUT_PATH = 'output/fdy'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('CV', 'http://limpica.net/fdy/cv'),)

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
