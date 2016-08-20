#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = ['pelican_alias']

AUTHOR = u'Bill Agee'
SITENAME = u"Bill Agee's blog"
SITESUBTITLE = u'🤔 Reflections on test infrastructure, with a twist of user empathy.'
SITEURL = ''

PATH = 'content'

# Title menu options
MENUITEMS = [('Blog', '/'),
             ('Archives', '/archives.html')]
NEWEST_FIRST_ARCHIVES = True

THEME = '/Users/bill/github/billagee/pelican-octopress-theme'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# Don't categories on main navigation menu
DISPLAY_CATEGORIES_ON_MENU = False
#CATEGORY_URL = ''
#CATEGORY_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('WatirMelon', 'https://watirmelon.com/'),
         ("A Seasoned Tester's Crystal Ball", 'http://visible-quality.blogspot.com/'),
         ('Software Quality Assurance and Test', 'https://dmcnulla.wordpress.com/'),)

# Social widget
#SOCIAL = (('stack-overflow', 'http://stackoverflow.com/users/267263/bill-agee'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TWITTER_USER = 'obvioso'
#TWITTER_WIDGET_ID = 
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = False
TWITTER_SHOW_FOLLOWER_COUNT = False

GITHUB_USER = 'billagee'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

SIDEBAR_IMAGE = "images/moderntimes.gif"
#SIDEBAR_IMAGE = "images/lucy.png"
SIDEBAR_IMAGE_ALT = "Sidebar image"
#SIDEBAR_IMAGE_WIDTH = Width of sidebar image
SEARCH_BOX = False
#SITESEARCH = [default: 'http://google.com/search'] s

# Moved to publishconf.py to avoid talking to GA during testing
#GOOGLE_ANALYTICS = "UA-30353441-1"
