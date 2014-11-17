# -*- coding: utf-8 -*-

from datetime import timedelta

def ensure_list(x):
    return x if isinstance(x, list) else [x]

def get_categories(pages):
    # useful for group-by categories if collate_content plugin can't be used
    return set(p.category for p in pages)

def as_timedelta(dt):
    # used for Duration header # TODO: this should probably be a plugin
    return timedelta(hours=dt.hour, minutes=dt.minute)

JINJA_FILTERS = {
    """ Don't use lambda functions because they don't pickle. """
    'ensure_list': ensure_list,
    'get_categories': get_categories,
    'as_timedelta': as_timedelta,
}
