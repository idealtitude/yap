#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
from shlex import split as shlex_split
from collections import deque
import argparse

from ycomp.htmldoc import DomTree

__version__ = '0.1'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()

parser = argparse.ArgumentParser(prog='yap', description='YAP, Yet Another -html pre- Processor', epilog='Help and documentation at https://github.com/idealtitude/yap')

parser.add_argument('file', nargs=1, help='The yap file to transpile to html')
parser.add_argument('-o', '--output', nargs='?', help='The destination file to output the html')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

args = parser.parse_args()


def yap_parser(input_file, output_file):
    f = open(input_file, 'r')
    c = f.read().splitlines()
    f.close()

    t_empty     = r'^\s*$'
    t_comment   = r'---.*$'
    t_indent    = r'(?P<indent>\t+)'
    t_attrs     = r'(?P<attrname>#|\.|[a-z0-9-]+)(?:`)(?P<attrvalue>.*)(?:`)$'

    lineno = 0
    #indsz = 0
    domstack = []

    for entry in c:
        lineno += 1

        if entry == '!5':
            domstack.append({'doctype': 'html5'})
            continue

        if (m := re.match(t_empty, entry)):
            continue

        if (m := re.match(t_comment, entry)):
            continue

        curind = 0
        if (m := re.match(t_indent, entry)):
            curind = len(m.group('indent'))

        elem = {
            'tag': None,
            'indent': curind,
            'attrs': [],
            'text': None,
            'autoclose': 1
        }

        line = deque(shlex_split(entry))

        if line[-1] == ';':
            line.pop()
            elem['autoclose'] = 0

        tag = line.popleft()

        attrs = []
        text = None

        if tag.endswith(':'):
            tag = tag.replace(':', '')

            x = 0
            for i in line:
                if i == '~':
                    break
                if (m := re.match(t_attrs, i)):
                    atn = m.group('attrname')
                    atv = m.group('attrvalue')

                    if atn == '#':
                        atn = 'id'
                    if atn == '.':
                        atn = 'class'

                    ta = (atn, atv)
                    attrs.append(ta)
                    x += 1

            for n in range(0, x):
                line.popleft()

        elem['tag'] = tag

        if len(attrs) > 0:
            elem['attrs'] = attrs
        else:
            elem['attrs'] = None

        text = ' '.join(line)
        text = re.sub('^~ ', '', text)
        if text == '':
            text = None
        elem['text'] = text

        domstack.append(elem)

    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file)
    dt = DomTree(domstack, html_file)
    dt.create_doc()

def main(args):
    if args.file:
        print(type(args.file))
        f_in = None
        if os.path.isfile(args.file[0]):
            f_in = args.file[0]

        f_out = None
        if args.output:
            f_out = args.output
        else:
            f_out = f'{APP_CWD}/yap.out.html'

        yap_parser(f_in, f_out)

        return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main(args))

