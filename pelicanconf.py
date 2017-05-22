#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ccl & Fdy'
SITENAME = u'LIMPICA'
SITEURL = '/staging'
SITESUBTITLE1 = 'Ccl. Picard & Fdy. Limpens'
SITESUBTITLE2 = 'works & ideas'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

THEME_STATIC_DIR = 'static'
PATH = 'content'
STATIC_PATHS = [ 'images','mail','js', 'css', 'fonts']
EXTRA_PATH_METADATA = {
    'static/images/portfolio': {'path': 'images/portfolio'},
    }
OUTPUT_PATH = 'output/staging'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Top Menu Links
NAVLINKS = (
	('#page-top', ''),
	('#portfolio', 'Portfolio'),
    #('#notes', 'Notes'),
	('#about', 'About'),
	('#contact', 'Contact')
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

THEME = "../pelican-free-agent-limpica"

# ** all settings below are specific to freeagent-limpica theme **

BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'
SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
    'imagesloaded.pkgd.min.js',
    'isotope.pkgd.min.js',
    'freeagent.js',
]

DIRECT_TEMPLATES = ['index']

# Portfolio Name
PORTFOLIO = 'Portfolio'
# Notes Name
NOTES = 'Notes'

ADDRESS1 = 'FRANCE - ITALY'

# Left column
ABOUT_1 = 'Cécile Picard-Limpens is a freelance in design, development and management of innovative projects at the crossroads of art, science and digital. After graduating as an acoustic engineer, she obtained her PhD in Computer Science (INRIA, Sophia-Antipolis) on Modeling and Sound Synthesis for Virtual Environments, then worked at the Haute Ecole de Musique in Genève (CH) and to Numédiart (Mons, BE) on research projects combining sound synthesis and human-machine interaction. '
# Right column
ABOUT_2 = 'Freddy Limpens is a freelance worker providing consulting, teaching, and complete realizations in web applications, linked data, e-learning, and digital fabrication. After graduating as a mechanical engineer, he completed a PhD in computer science at Inria (studying social web data and Linked Data principles). Since then, he contributes, as a fullstack developper and consultant,  to projects ranging from collaborative web platforms, to e-learning eco-systems and digital fabrication. See <a href="http://limpica.net/fdy/cv/">his cv</a> for more details.'
# Center
ABOUT_CENTER = '</br>What we perceive constructs us. We are what we feel, what we see, what we hear. But perception is not a faculty per se, it is printed from what we are.. our observation point is localised by our own body, which, just by filling a volume, might influence the observation itself... so the question loops and never ends. This mere question is endless and simply virtiginuous. We have no aim to answer it, just the desire to explore the complexity of the imbrication. The <em>objectivity</em> of the camera will not overcome the ambiguity of perception. However, we consider the camera as a tool for exploring what we may perceive, a window opened on our subconscience.</a>'
