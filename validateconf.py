#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make validate`
import os; os.sys.path.insert(1, os.curdir)
from publishconf import *

PLUGINS.extend([
    'w3c_validate'
])

for plugin in ('minify',  # don't minify when validating
               'warnings_fatal'):  # validate through the end
    PLUGINS.remove(plugin)
