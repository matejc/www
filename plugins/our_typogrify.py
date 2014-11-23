"""
Apply Typogrify filters.

We don't use Pelican-built-in TYPOGRIFY=True because that
messes with other plugins: jinja2content, Markdown's attr_list, ...
"""

from pelican import signals
from typogrify.filters import typogrify as _typogrify

def apply_typogrify(page):
    if page.settings['TYPOGRIFY']:
        raise RuntimeError('No, we said non-plugin-Typogrify is NOT OK')

    def typogrify(text):
        return _typogrify(text, page.settings['TYPOGRIFY_IGNORE_TAGS'])

    if page._content:
        page._content = typogrify(page._content)
        page._summary = typogrify(page._get_summary())
        page.title = typogrify(page.title)
    for key in ('title', 'summary'):
        if key in page.metadata:
            page.metadata[key] = typogrify(page.metadata[key])

def register():
    signals.content_object_init.connect(apply_typogrify)
