# -*- coding: utf-8 -*-

import re

from typing import NamedTuple, Tuple, Pattern


class Tokens(NamedTuple):
    t_empty: Tuple[Pattern[str]] = re.compile(r'^\s*$'),
    t_yapcomment: Tuple[Pattern[str]] = re.compile('---.*$'),
    t_indent: Tuple[Pattern[str]] = re.compile('^(?P<indent>\t+)'),
    t_attrs: Pattern[str] = re.compile(r'(?P<attrname>#|\.|[a-z0-9-]+)(?:`)(?P<attrvalue>.*?)(?:`)')

