from pelican import signals
from pelican.utils import get_date, set_date_tzinfo, strftime
from operator import attrgetter
from copy import copy
import logging

log = logging.getLogger(__name__)

def duplicate_on_dates(generator):
    """
    Articles (events) with `dates` property are recurring. Create a
    copy of the article for each date in `dates`.
    """
    articles = []
    for article in generator.articles:
        if not hasattr(article, 'dates'):
            articles.append(article)
            continue
        log.debug('Event {} has {} occurrences.'.format(article.get_relative_source_path(), len(article.dates)))
        for i, date in enumerate(article.dates, 2):
            event = copy(article)
            articles.append(event)
            event.slug += '--' + str(i)  # Create hopefully unique slug
            # The comment following '#' can be anything (e.g. visitor count)
            date, _, event.dates_comment = date.partition('#')
            # From pelican.contents.Content.__init__
            timezone = getattr(event, 'timezone', event.settings.get('TIMEZONE', 'UTC'))
            event.date = set_date_tzinfo(get_date(date), timezone)
            event.locale_date = strftime(event.date, event.date_format)
    articles.sort(key=attrgetter(generator.settings['ARTICLE_ORDER_BY']), reverse=True)
    generator.articles = articles
    

def register():
    signals.article_generator_pretaxonomy.connect(duplicate_on_dates)
