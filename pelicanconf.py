#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

AUTHOR = 'Hadrien Mary'
SITENAME = 'Hadrien Mary'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('LBCMCP: my lab',
         'http://www-lbcmcp.ups-tlse.fr'),
         ('Tournier-Gachet Team: my lab team',
          'http://www-lbcmcp.ups-tlse.fr/Nouveau_site/modeles/EquipeTournier-Accueil.htm'),
         ('damcb.com: Guillaume Gay, an independant collaborator',
          'http://damcb.com/'))

# Social widget
SOCIAL = (('Mail: you can use this mail',
          'mailto:hadrien.mary AT univ-tlse3 DOT fr'),
          ('GMail: or this one',
           'mailto:hadrien.mary AT gmail DOT com'),
          ('GitHub: what I code',
           'https://github.com/hadim'),
          ("Linkedin: professional profile", "http://fr.linkedin.com/in/hadimary"),
          ('Google+: personal profile (not so much filled)',
           'https://plus.google.com/100297872480160783190/'),
          ('Google Scholar: academic publications (nothing yet!)',
           'http://scholar.google.com/citations?user=gGjpl6kAAAAJ'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/hadim"

STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/CNAME': {'path': 'CNAME'}
                       }

PAGE_PATHS = ['']
PAGE_EXCLUDES = ['posts']
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = []

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}/index.html'

CATEGORY_SAVE_AS = False
ARCHIVE_SAVE_AS = False
AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False

MENUITEMS = ()

INDEX_PAGE = "research"
NAVIGATION_BAR = [('research', 'Research'),
                  ('softwares', 'Softwares'),
                  ('visualization', 'Visualization'),
                  ('cv', 'CV'),
                  ('previous-work', 'Previous Work'),
                  ('contact', 'Contact')]

now = datetime.datetime.now()
LAST_UPDATE = now.strftime("%d/%m/%Y")

FEED_DOMAIN = None
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
