#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bill Agee'
SITENAME = u"Bill Agee's blog"
SITESUBTITLE = u'Technology musings with a twist of user empathy.'
SITEURL = ''

PATH = 'content'

# Title menu options
MENUITEMS = [('Blog', '/'),
             ('Archives', '/archives.html')]
NEWEST_FIRST_ARCHIVES = False

THEME = "/Users/bill/github/billagee/pelican-octopress-theme"

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/billagee'),
          ('stack-overflow', 'http://stackoverflow.com/users/267263/bill-agee'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
