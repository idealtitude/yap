#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YAP (Yet Another -html- Preprocessor)

Input a yap file (see doc/help.md or man yap for definition
of the yap files format) and output a nice html file.
"""

import sys

if sys.version_info < (3, 10, 0):
    raise RuntimeError("Python 3.10 or later required")

import os
from typing import Any
import argparse

#from utils.filehandler import BasicFIle
from utils.appinit import AppInit

# App infos
__author__ = "idealtitude"
__version__ = "0.3.0"
__license__ = "ISC"

# Constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
#APP_PATH = os.path.dirname(os.path.realpath(__file__))
#APP_CWD = os.getcwd()

# Command line arguments
def get_args() -> argparse.Namespace:
    """Basic arguments parsing."""

    parser = argparse.ArgumentParser(
        prog="yap",
        description="YAP, Yet Another -html pre- Processor",
        epilog="Help and documentation at https://github.com/idealtitude/yap",
    )

    parser.add_argument("file", nargs=1, help="The yap file to transpile to html")
    parser.add_argument(
        "-o", "--output", nargs=1, help="The destination file to output the html"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser.parse_args()


def main() -> int:
    """Entry point"""

    args: argparse.Namespace = get_args()

    if args.file:
        file_out: str = "default"

        if args.output:
            file_out = args.output[0]

        pathes = {
            "root": os.path.dirname(os.path.realpath(__file__)),
            "cwd": os.getcwd(),
            "home": os.path.expanduser('~'),
            "input": args.file[0],
            "output": file_out
        }

        app = AppInit(pathes)

        if not app.init_ok:
            print("Error while initializing yap...")
            return EXIT_FAILURE

        transpiler_data: dict[str, str] = {
            "input": app.app_pathes["input"],
            "output": app.app_pathes["output"],
            "indent": app.settings["output"]["indent_type"],
            "size": app.settings["output"]["indent_size"]
        }

        print(f"App intialized with values:\n{transpiler_data}")

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
