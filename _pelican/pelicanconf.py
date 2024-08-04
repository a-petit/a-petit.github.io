from pelican.readers import MarkdownReader
from pelican.settings import DEFAULT_CONFIG

AUTHOR = 'Alexandre Petit'
SITENAME = 'Alexandre Petit'
SITEURL = ""

PATH = "content"
THEME = 'themes/a-petit'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

HOME, _ = MarkdownReader(DEFAULT_CONFIG.copy()).read("content/pages/home.md")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Désactive la génération des pages suivantes
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
