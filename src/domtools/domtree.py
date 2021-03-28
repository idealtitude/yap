# -*- coding: utf-8 -*-

import re

import utils.patterns as uptn

t_empty     = uptn.PATTERNS['t_empty']
t_comment   = uptn.PATTERNS['t_comment']
t_indent    = uptn.PATTERNS['t_indent']
t_attrs     = uptn.PATTERNS['t_attrs']

class NodeManager:
    def __init__(self):
        self.node = {
            'tag': None,
            'attrs': None,
            'autoclose': False,
            'content': None,
            'indent': None,
            'state': 0 # 0 -> open, 1 -> closed
        }


class CreateElem:
    def __init__(self, entry):
        self.entry = entry
        self.elem = NodeManager()

        self.construct_node()
        self.get_content()

    def construct_node(self):
        indsz = 0
        if (m := t_indent.match(self.entry)):
            indsz = len(m.group('indent'))

        self.elem.node['indent'] = indsz

        if self.entry.endswith(';'):
            self.elem.node['autoclose'] = True
            self.entry = re.sub(';$', '', self.entry)

        self.entry = self.entry.strip()

        self.get_tag()

    def get_tag(self):
        tmp = self.entry.split(' ', 1)
        tag = tmp[0]
        tag = tag.strip()

        self.entry = re.sub(fr'^{tag}', '', self.entry)
        self.entry = self.entry.strip()

        if tag.endswith(':'):
            tag = tag.replace(':', '')
            self.get_attrs()

        self.elem.node['tag'] = tag

    def get_attrs(self):
        attrs = ''
        if (m := t_attrs.finditer(self.entry)):
            for a in m:
                self.entry = self.entry.replace(a.group(), '')
                atn = a.group('attrname')
                atv = a.group('attrvalue')

                if atn == '#':
                    atn = 'id'
                elif atn == '.':
                    atn = 'class'

                tmp = f' {atn}="{atv}"'
                attrs += tmp

        self.entry = self.entry.strip()

        if attrs != '':
            self.elem.node['attrs'] = attrs

    def get_content(self):
        tmp = self.entry
        if tmp.startswith('~'):
            tmp = re.sub('^~', '', tmp)
            tmp = tmp.strip()
            self.elem.node['content'] = tmp

        self.entry = None

