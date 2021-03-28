#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import argparse

import utils.patterns as uptn
import domtools.domtree as dtree

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


def transpiler(input_file, output_file):
    fd = open(input_file, 'r')
    file_content = fd.read().splitlines()
    fd.close()

    t_empty     = uptn.PATTERNS['t_empty']
    t_comment   = uptn.PATTERNS['t_comment']
    t_indent    = uptn.PATTERNS['t_indent']
    t_attrs     = uptn.PATTERNS['t_attrs']

    lineno = 0
    domstack = []
    source = ''

    for entry in file_content:
        lineno += 1

        if entry == '!5':
            source = '<!DOCTYPE html>'
            continue

        if (m := t_empty.match(entry)):
            continue

        if (m := t_comment.match(entry)):
            continue

        element = dtree.CreateElem(entry)
        domstack.append(element.elem)

    treestack = []
    indsz = 0

    for elem in domstack:
        node = elem.node

        indent = node['indent']
        ind = '    ' * indent
        tag = node['tag']

        attrs = ''
        if node['attrs'] != None:
            attrs = node['attrs']

        if indent >= indsz:
            if node['autoclose']:
                source += f'\n{ind}<{tag}{attrs}>'
            elif node['content'] != None:
                source += f'\n{ind}<{tag}{attrs}>{node["content"]}</{tag}>'
            else:
                source += f'\n{ind}<{tag}{attrs}>'
                treestack.append(tag)
        elif indent < indsz:
            rng = indsz - indent
            if rng == 1:
                t = treestack.pop()
                source += f'\n{ind}</{t}>'
            else:
                tind = '    ' * (len(treestack) - 1)
                for n in range(rng):
                    t = treestack.pop()
                    source += f'\n{tind}</{t}>'
                    tind = re.sub('^ {4}', '', tind)

            if node['autoclose']:
                source += f'\n{ind}<{tag}{attrs}>'
            elif node['content'] != None:
                source += f'\n{ind}<{tag}{attrs}>{node["content"]}</{tag}>'
            else:
                source += f'\n{ind}<{tag}{attrs}>'
                treestack.append(tag)
        indsz = indent

    sz = len(treestack)

    if sz > 0:
        tind = '    ' * (sz - 1)
        for e in range(sz):
            t = treestack.pop()
            source += f'\n{tind}</{t}>'
            tind = re.sub('^ {4}', '', tind)

    #print(source)
    fd = open(output_file, 'w')
    fd.write(source)
    fd.close()

def main(args):
    if args.file:
        f_in = None
        if os.path.isfile(args.file[0]):
            f_in = args.file[0]

        f_out = None
        if args.output:
            f_out = args.output
        else:
            f_out = f'{APP_CWD}/yap.out.html'

        transpiler(f_in, f_out)

        return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main(args))
