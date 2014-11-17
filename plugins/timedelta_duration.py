from pelican import signals
from datetime import datetime, timedelta
import logging

log = logging.getLogger(__name__)

def timedelta_duration(generator):
    """
    Replace `duration` article properties in '%H:%M' format with
    timedelta objects. Also add `end_date` as `date` + `duration`.
    """
    for article in generator.articles:
        if hasattr(article, 'duration'):
            log.debug('Event {} has duration: {}'.format(article.get_relative_source_path(), article.duration))
            time = datetime.strptime(article.duration, '%H:%M')
            article.duration = timedelta(hours=time.hour, minutes=time.minute)
            article.end_date = article.date + article.duration

def register():
    signals.article_generator_finalized.connect(timedelta_duration)
