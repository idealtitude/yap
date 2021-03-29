#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import argparse
import errno

import utils.patterns as uptn
from utils.yapconfig import ConfManager
import domtools.domtree as dtree

__version__ = '0.2'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()

parser = argparse.ArgumentParser(prog='yap', description='YAP, Yet Another -html pre- Processor', epilog='Help and documentation at https://github.com/idealtitude/yap')

parser.add_argument('file', nargs=1, help='The yap file to transpile to html')
parser.add_argument('-o', '--output', nargs='?', help='The destination file to output the html')
#parser.add_argument('-i', '--indent', nargs=1, type=int, help='The size of indentation for the output html (default: 4 self.spaces')
#parser.add_argument('-t', '--type', nargs=1, choices=['tab', 'space'], help='The type of indentation for the output html')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

args = parser.parse_args()

def get_config():
    conf = ConfManager(APP_PATH)
    indent_type = conf.config['output']['indent_type']
    indent_size = conf.config['output']['indent_size']
    indentation = None
    if indent_type == 'space':
        indentation = ' ' * indent_size
    elif indent_type == 'tab':
        indentation = '\t' * indent_size

    return (indentation, f'{APP_CWD}/{conf.config["output"]["output_file"]}')

class Yap:
    def __init__(self, filein, fileout, indent):
        self.domstack = []
        self.source = ''
        self.input_file = filein
        self.output_file = fileout
        self.spaces = indent

    def transpiler_in(self):
        fd = open(self.input_file, 'r')
        file_content = fd.read().splitlines()
        fd.close()

        t_empty     = uptn.PATTERNS['t_empty']
        t_comment   = uptn.PATTERNS['t_comment']
        #t_indent    = uptn.PATTERNS['t_indent']
        #t_attrs     = uptn.PATTERNS['t_attrs']

        lineno = 0
        self.domstack = []
        #self.source = ''

        for entry in file_content:
            lineno += 1

            if entry == '!5':
                self.source = '<!DOCTYPE html>\n'
                continue

            if (_m := t_empty.match(entry)):
                continue

            if (_m := t_comment.match(entry)):
                continue

            element = dtree.CreateElem(entry)
            self.domstack.append(element.elem)

        return self.domstack

    def transpiler_out(self):
        treestack = []
        indsz = 0

        for elem in self.domstack:
            node = elem.node

            indent = node['indent']
            ind = self.spaces * indent
            tag = node['tag']

            attrs = ''
            if node['attrs'] != None:
                attrs = node['attrs']

            if indent >= indsz:
                if node['autoclose']:
                    self.source += f'{ind}<{tag}{attrs}>\n'
                elif node['content'] != None:
                    self.source += f'{ind}<{tag}{attrs}>{node["content"]}</{tag}>\n'
                else:
                    self.source += f'{ind}<{tag}{attrs}>\n'
                    treestack.append(tag)
            elif indent < indsz:
                rng = indsz - indent
                if rng == 1:
                    t = treestack.pop()
                    self.source += f'{ind}</{t}>\n'
                else:
                    tind = self.spaces * (len(treestack) - 1)
                    for _n in range(rng):
                        t = treestack.pop()
                        self.source += f'{tind}</{t}>\n'
                        tind = re.sub('^ {4}', '', tind)

                if node['autoclose']:
                    self.source += f'{ind}<{tag}{attrs}>\n'
                elif node['content'] != None:
                    self.source += f'{ind}<{tag}{attrs}>{node["content"]}</{tag}>\n'
                else:
                    self.source += f'{ind}<{tag}{attrs}>\n'
                    treestack.append(tag)
            indsz = indent

        sz = len(treestack)

        if sz > 0:
            tind = self.spaces * (sz - 1)
            for _e in range(sz):
                t = treestack.pop()
                self.source += f'{tind}</{t}>\n'
                tind = re.sub('^ {4}', '', tind)

        #print(self.source)
        fd = open(self.output_file, 'w')
        fd.write(self.source)
        fd.close()

def main(args):
    if args.file:
        config = get_config()
        indent = config[0]
        f_out = config[1]

        f_in = None
        if os.path.isfile(args.file[0]):
            f_in = args.file[0]
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f_in)

        if args.output:
            f_out = args.output

        new_yap = Yap(f_in, f_out, indent)

        new_yap.transpiler_in()
        new_yap.transpiler_out()

        return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main(args))
