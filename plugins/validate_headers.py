from __future__ import unicode_literals
from pelican import signals, contents
from os import path
import logging
import yaml

log = logging.getLogger(__name__)

CONFIG_FILE = '_config.yml'

valid_tags, valid_categories = set(), set()


def create_valid_sets(pelican):
    """ Create valid sets. """

    global valid_tags, valid_categories
    with open(path.join(pelican.settings['PATH'], "../", CONFIG_FILE)) as f:
        obj = yaml.load(f)

    content = obj["prose"]["metadata"][obj["prose"]["rooturl"]]

    def get_valid(field):
        for f in content:
            if f['name'] == field:
                return f['field']['options']

    valid_tags = set(i["value"] for i in get_valid("tags"))
    valid_categories = set(i["value"] for i in get_valid("category"))

    log.debug('Valid categories: ' + str(valid_categories))
    log.debug('Valid tags: ' + str(valid_tags))


class NoCategoryException(Exception):
    pass


class NoTagsException(Exception):
    pass


def validate_tags_categories(generator, article):
    """
    Ensure all tags and categories used in articles are valid (i.e.
    present in content/{tags,categories}.txt).
    """
    assert type(article) == contents.Article
    if (not getattr(article, 'published', True)  # set by Prose.io
        or  getattr(article, 'status', '') == 'draft'):
        article.status = 'draft'  # expected by Pelican
        return  # Skip drafts
    try:
        # Ensure category is valid
        category = article.category.name
        if category not in valid_categories:
            log.error("{}: Invalid category '{}', or valid and missing in {}".format(
                article.get_relative_source_path(), category, CONFIG_FILE))
    except (KeyError, AttributeError):
        raise NoCategoryException("Article is missing a category!")
    try:
        # Ensure tags are valid
        for tag in article.tags:
            if tag.name not in valid_tags:
                log.error("{}: Invalid tag '{}', or valid and missing in {}".format(
                    article.get_relative_source_path(), tag, CONFIG_FILE))
    except (KeyError, AttributeError):
        raise NoTagsException("Article has no tags!")


def register():
    signals.content_object_init.connect(validate_tags_categories, sender=contents.Article)
    signals.initialized.connect(create_valid_sets)
