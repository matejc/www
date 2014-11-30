"""
This extension modifies the output of md_meta_yaml plugin so that
all values are strings as Pelican expects them.

Once Python-Markdown>=2.6 hits, and when Pelican is ready to accept
pre-parsed YAML objects, md_meta_yaml and this extension can both
be deleted!

"""

from __future__ import absolute_import, unicode_literals
import markdown
import datetime

class MetaDateStrExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        """Add MetaYamlPreprocessor to Markdown instance."""
        md.preprocessors.add("yaml_date_str",
                             MetaDateStrPreprocessor(md),
                             ">meta_yaml")  # add after md_meta_yaml


class MetaDateStrPreprocessor(markdown.preprocessors.Preprocessor):
    def run(self, lines):
        # Meta is already in self.markdown.Meta, just need to stringify dates
        Meta = self.markdown.Meta
        for key in Meta:
            for i, el in enumerate(Meta[key]):
                if isinstance(el, datetime.date):
                    Meta[key][i] = el.isoformat()
        # that's it
        return lines


def makeExtension(configs={}):
    """set up extension."""
    return MetaDateStrExtension(configs=configs)
