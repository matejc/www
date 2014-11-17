#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os; os.sys.path.insert(1, os.curdir)
from pelicanconf import *

SITEURL = 'http://www.kiberpipa.org'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = '' # TODO
DISQUS_SITENAME = 'kiberpipa'  # TODO

PLUGINS.extend([
    'minify',         # strips HTML of excessive whitespace
    'warnings_fatal',   # ours; makes warnings fatal
])

WARNINGS_FATAL = True

