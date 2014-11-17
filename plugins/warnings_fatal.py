""" Monkey-patches logging so that warnings become fatal. """

from pelican import signals
import sys, logging

log = logging.getLogger(__name__)

critical = log.critical

def new_handler(etype):
    old_handler = getattr(logging.Logger, etype)
    def f(*args, **kwargs):
        old_handler(*args, **kwargs)
        critical(etype.capitalize() + ' encountered and not allowed.')
        sys.exit(1)
    return f

def make_warnings_fatal(pelican):
    if pelican.settings.get('WARNINGS_FATAL'):
        logging.Logger.critical = new_handler('critical')
        logging.Logger.warning = new_handler('warning')
        logging.Logger.error = new_handler('error')

def register():
    signals.initialized.connect(make_warnings_fatal)
