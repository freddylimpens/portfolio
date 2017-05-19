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
	'freeagent.js',
    'isotope.pkgd.min.js',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']

# Top Menu Links
NAVLINKS = (
	('#page-top', ''),
	('#portfolio', 'Portfolio'),
    #('#notes', 'Notes'),
	('#about', 'About'),
	('#contact', 'Contact')
)

# Portfolio Name
PORTFOLIO = 'Portfolio'
# Notes Name
NOTES = 'Notes'

#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],
	['Phone Number', 'tel', 'phone', 'Please enter your phone number.'],
	['Message', 'textarea', 'message', 'Please enter a message.']
)

ADDRESS1 = 'FRANCE - ITALY'

# Left column
ABOUT_1 = 'After graduating as an acoustic engineer, Cécile Picard-Limpens obtained her PhD in Computer Science (INRIA, Sophia-Antipolis) on Modeling and Sound Synthesis for Virtual Environments, then worked at the Haute Ecole de Musique in Genève (CH) and to Numédiart (Mons, BE) on research projects combining sound synthesis and human-machine interaction. '
# Right column
ABOUT_2 = 'Freddy Limpens received a PhD from INRIA where he worked on tagging and folksonomies, seeking novel ways to interconnect Social Web and Semantic Web.'
# Center
ABOUT_CENTER = '</br>What we perceive constructs us. We are what we feel, what we see, what we hear. But perception is not a faculty per se, it is printed from what we are.. our observation point is localised by our own body, which, just by filling a volume, might influence the observation itself... so the question loops and never ends. This mere question is endless and simply virtiginuous. We have no aim to answer it, just the desire to explore the complexity of the imbrication. The <em>objectivity</em> of the camera will not overcome the ambiguity of perception. However, we consider the camera as a tool for exploring what we may perceive, a window opened on our subconscience.</a>'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)



# THEME = "../pelican-themes/simple-bootstrap"
# THEME = "../pelican-themes/photowall"
# THEME = "../pelican-themes/pure"
THEME = "../pelican-free-agent-limpica"
# THEME = "../../minimalist-portfolio"
