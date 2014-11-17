from __future__ import unicode_literals
from pelican import signals, contents
from os import path
import logging

log = logging.getLogger(__name__)

TAGS_FILE = 'tags.txt'
CATEGORIES_FILE = 'categories.txt'

valid_tags, valid_categories = set(), set()

def to_utf8(str):
    # Python 2 compatibility
    return str.decode('utf-8') if hasattr(str, 'decode') else str

def create_valid_sets(pelican):
    """ Create valid sets. """
    global valid_tags, valid_categories
    for fname, valid in ((TAGS_FILE, valid_tags),
                         (CATEGORIES_FILE, valid_categories)):
        with open(path.join(pelican.settings['PATH'], fname)) as f:
            for line in f:
                line = to_utf8(line).partition('#')[0].strip()  # Strip comments
                if ',' in line:
                    log.error('Tags in {} must be one per line!'.format(fname))
                if line:
                    valid.add(line)
    log.debug('Valid categories: ' + str(valid_categories))
    log.debug('Valid tags: ' + str(valid_tags))

class NoCategoryException(Exception): pass
class NoTagsException(Exception): pass

def validate_tags_categories(generator, article):
    """
    Ensure all tags and categories used in articles are valid (i.e.
    present in content/{tags,categories}.txt).
    """
    if getattr(article, 'status', '') == 'draft':
        return  # Skip drafts
    try:
        # Ensure category is valid
        category = article.category.name
        if category not in valid_categories:
            log.error("{}: Invalid category '{}', or valid and missing in {}".format(
                article.get_relative_source_path(), category, CATEGORIES_FILE))
    except (KeyError, AttributeError):
        raise NoCategoryException("Article is missing a category!")
    try:
        # Ensure tags are valid
        for tag in article.tags:
            if tag.name not in valid_tags:
                log.error("{}: Invalid tag '{}', or valid and missing in {}".format(
                    article.get_relative_source_path(), tag, TAGS_FILE))
    except (KeyError, AttributeError):
        raise NoTagsException("Article has no tags!")

def register():
    signals.content_object_init.connect(validate_tags_categories, sender=contents.Article)
    signals.initialized.connect(create_valid_sets)
