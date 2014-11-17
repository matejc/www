#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os; os.sys.path.insert(1, os.curdir)

# Useful in development, but set to False when publishing!
RELATIVE_URLS = True

AUTHOR = 'Kiberpipa'
SITENAME = 'Kiberpipa'
SITEURL = 'http://www.kiberpipa.org'
SITESUBTITLE = 'All our code are belong to you.'
TIMEZONE = 'Europe/Ljubljana'
DEFAULT_LANG = 'sl'
LOCALE = ('sl_SI', 'en_US', 'en')
DEFAULT_DATE_FORMAT = '%a, %d %b %Y -- %H:%M'
DATE_FORMATS = {
    'sl': '%A, %d. %B, %Y -- %H:%M',
    'en': '%a, %d %b %Y -- %I:%M %p',
}

TWITTER_USERNAME = 'Kiberpipa'

MENUITEMS = ()  # Additional (Title, URL) pairs
DEFAULT_METADATA = ()  # for all articles/pages
WITH_FUTURE_DATES = True  # support future events
SUMMARY_MAX_LENGTH = 50  # words

PATH = 'content'  # path all else is relative to (except when it's relative to this .py file)
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['events', 'news']

LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
CACHE_PATH = 'cache'
GZIP_CACHE = False

# Blogroll
LINKS = (
    ('CoderDojo Ljubljana', 'http://ljubljana.coderdojo.si'),
    ('OpenData Slovenia', 'http://opendata.si'),
    ('Bitcoin društvo Slovenije', 'http://bitcoin.si'),
    ('SloGameDev', 'http://www.slogamedev.net/'),
)

# Social widget
SOCIAL = (
    ('Facebook', 'http://facebook.com/kiberpipa'),
    ('Twitter', 'http://twitter.com/Kiberpipa'),
    ('YouTube', 'http://youtube.com/kiberpipa'),  # TODO
    ('GitHub', 'http://github.com/kiberpipa'),
)

PLANET = (  # TODO: implement
    ("Matej Cotman's Blog", 'http://blog.matejc.com'),
    ("Jaka Hudoklin", 'http://jakahudoklin.com/'),
    ("Hook's Humble Homepage", 'http://matija.suklje.name'),
    ("Domen Kožar's Thoughts", 'https://www.domenkozar.com/'),
    ("Avian's Blog", 'http://www.tablix.org/~avian/blog/'),
)

# Pagination
DEFAULT_PAGINATION = 10  # paginate every 10 entries
DEFAULT_ORPHANS = 3      # min 3 entries on last page
PAGINATION_PATTERNS = (  # /basename/, /basename/page/2, /basename/page/3, ...
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

## Output Generation
## ====================================================================

DELETE_OUTPUT_DIRECTORY = True  # prevent stale output files
OUTPUT_RETENTION = ('.git')  # this directory is not deleted
IGNORE_FILES = ['.#*', '.*', '#*']  # don't process files that match these globs
STATIC_PATHS = [  # copy these PATH-relative paths to output
    'images',
    'extra/robots.txt',
    'extra/CNAME',       # custom domain on GitHub pages
    'extra/404.html',    # custom 404 error page
]
EXTRA_PATH_METADATA = {}
# copy everything in content/extra to www root
EXTRA_PATH_METADATA.update({f:{'path': f[6:]} for f in STATIC_PATHS if f.startswith('extra/')})

## URL router
## ====================================================================

# Extract date and slug from filename, if available
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}(T\d{2}:\d{2})?)_(?P<slug>.*)'

SLUG_SUBSTITUTIONS = [(r[:-1], r[-1:]) for r in ('čc', 'šs', 'žz', 'Čc', 'Šs', 'Žz',
                                                 'áa', 'ée', 'íi', 'óo', 'úu',
                                                 'Áa', 'Ée', 'Íi', 'Óo', 'Úu',
                                                 'äa', 'ëe', 'ïi', 'öo', 'üu',
                                                 'Äa', 'Ëe', 'Ïi', 'Öo', 'Üu')] + \
                     [(r[:-2], r[-2:]) for r in ('đdz', 'Đdz')]

ARTICLE_URL = '{date:%Y}/{date:%m}/{category}/{slug}/'  # /2014/07/pot/sample-pot-event/
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_LANG_URL = '{lang}/' + ARTICLE_URL              # /en/2014/07/pot/sample-pot-event/
ARTICLE_LANG_SAVE_AS = '{lang}/' + ARTICLE_URL + 'index.html'
ARTICLE_ORDER_BY = 'date'

PAGE_URL = '{slug}/'                                    # /about/
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_LANG_URL = '{lang}/' + PAGE_URL                    # /en/about/
PAGE_LANG_SAVE_AS = '{lang}/' + PAGE_URL + 'index.html'
PAGE_ORDER_BY = 'basename'

DRAFT_URL = 'draft/' + ARTICLE_URL                      # /draft/2014/07/pot/sample-pot-event/
DRAFT_SAVE_AS = DRAFT_URL + 'index.html'
DRAFT_LANG_URL = 'draft/{lang}/' + '/'.join(DRAFT_URL.split('/')[1:])  # /draft/en/2014/07/pot/sample-pot-event/

CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = CATEGORIES_URL + 'index.html'      # /category/
CATEGORY_URL = CATEGORIES_URL + '{slug}/'               # /category/pot/
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAGS_URL = 'tag/'
TAGS_SAVE_AS = TAGS_URL + 'index.html'                  # /tag/
TAG_URL = TAGS_URL + '{slug}/'                          # /tag/hackday/
TAG_SAVE_AS = TAG_URL + 'index.html'

AUTHORS_URL = 'alumni/'
AUTHORS_SAVE_AS = AUTHORS_URL + 'index.html'            # /alumni/
AUTHOR_URL = AUTHORS_URL + '{slug}/'                    # /alumni/nickname/
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'             # /2014/
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'  # /2014/07/

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

TEMPLATE_PAGES = {
    #'extra/calendar.ics.jinja2': 'calendar.ics'
}

## Atom/RSS Feeds
## ====================================================================

FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 20
FEED_USE_SUMMARY = True  # used by feed_summary plugin
FEED_ALL_ATOM = 'feeds/all/atom.xml'
FEED_ALL_RSS = 'feeds/all/rss.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s/atom.xml'
TRANSLATION_FEED_RSS = 'feeds/all-%s/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s/atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s/rss.xml'
AUTHOR_FEED_ATOM = 'feeds/author/%s/atom.xml'
AUTHOR_FEED_RSS = 'feeds/author/%s/rss.xml'
TAG_FEED_ATOM = 'feeds/tag/%s/atom.xml'
TAG_FEED_RSS = 'feeds/tag/%s/rss.xml'

## Themes
## ====================================================================

EXTRA_TEMPLATES_PATHS = []
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')
PAGINATED_DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')

THEME = 'theme'
THEME_STATIC_DIR = 'theme'  # relied on by webassets

## Plugins & extensions
## ====================================================================

TYPOGRIFY = True
from plugins.jinja2_filters import JINJA_FILTERS
JINJA_EXTENSIONS = [
    'jinja2.ext.i18n',
    'jinja2.ext.do',
    'jinja2.ext.loopcontrols',
]

MD_EXTENSIONS = [  # https://pythonhosted.org/Markdown/extensions/
    'meta',
    'extra',
    'admonition',
    'codehilite(css_class=highlight)',
    'sane_lists',
    'smarty(smart_angled_quotes=True)',
# 3rd-party
    'del_ins',
    'urlize:UrlizeExtension',
    'superscript',
]

PLUGIN_PATHS = [
    'pelican-plugins',
    'pelican-plugins/pelican-jinja2content',
    'pelican-3rd-plugins',
    'plugins',
]
# Some plugins are also in publishconf.py
PLUGINS = [
#
#  Zero-maintenance plugins; take effect automatically
#
    'bootstrapify',  # auto-bootstapifies markdown tables and images
    'feed_summary',  # use summary in RSS feeds
    'optimize_images',  # needs libjpeg-prog and optipng
    #'jinja2content',  # support for jinja2 include statement in articles
    'pelican-page-hierarchy', # support for breadcrumbs and nested pages
    'pelican-page-order',     # each page gets a page_order attribute useful for sorting
    'sitemap',        # generates sitemap.xml
    'pelican_alias',  # redirects Alias-ed URL to canonical one (prevents link rot)
    'multi_dates',    # ours; replicates recurring articles on Dates list
    'validate_headers',  # ours; validates article's category, tags, ...
#
#  Plugins template designers should be aware of:
#
    'assets',     # use {% assets %} to compile JS, CSS
    'neighbors',  # next_ and prev_article
    'collate_content',  # collates articles and pages in collations.{category}_articles/_pages groups
    'representative_image',  # have meta Image be featured_image article property
    'share_post',     # article.share_post dict of URLs
    'related_posts',  # adds article.related_posts list of articles that share a common tag
    'timedelta_duration',  # ours; makes duration a timedelta and adds end_date property
# also consider
# * https://github.com/getpelican/pelican-plugins/tree/master/custom_article_urls
# * https://github.com/getpelican/pelican-plugins/tree/master/disqus_static
# * https://github.com/getpelican/pelican-plugins/tree/master/gzip_cache
# * https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites
# * https://github.com/getpelican/pelican-plugins/tree/master/interlinks
# * https://github.com/Shaked/pin_to_top
# * https://github.com/getpelican/pelican-plugins/tree/master/simple_footnotes
# * https://github.com/getpelican/pelican-plugins/tree/master/subcategory # interesting because subcategory feeds
]

# Plugins' settings
SITEMAP = {'format':'xml'}
RELATED_POSTS_MAX = 10

