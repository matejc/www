# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
import pytz
from bs4 import BeautifulSoup

from pelican.utils import memoized

def ensure_list(x):
    return x if isinstance(x, list) else [x]

def get_categories(pages):
    # useful for group-by categories if collate_content plugin can't be used
    return set(p.category for p in pages)

def as_timedelta(dt):
    # used for Duration header # TODO: this should probably be a plugin
    return timedelta(hours=dt.hour, minutes=dt.minute)

def format_date(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)

def to_utc(dt):
    return dt.astimezone(pytz.utc)

@memoized
def html2text(html):
    return BeautifulSoup(html.replace('&nbsp;', ' ')).get_text()

JINJA_FILTERS = {
    """ Don't use lambda functions because they don't pickle. """
    'ensure_list': ensure_list,
    'get_categories': get_categories,
    'as_timedelta': as_timedelta,

    # for calendar.ics
    'dt_format': format_date,
    'to_utc': to_utc,
    'html2text': html2text,
}
