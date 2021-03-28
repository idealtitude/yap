# -*- coding: utf-8 -*-

import re


PATTERNS = {
    't_empty': re.compile(r'^\s*$'),
    't_comment': re.compile('---.*$'),
    't_indent': re.compile('^(?P<indent>\t+)'),
    't_attrs': re.compile(r'(?P<attrname>#|\.|[a-z0-9-]+)(?:`)(?P<attrvalue>.*?)(?:`)')
}