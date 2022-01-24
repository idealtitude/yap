#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YAP (Yet Another -html- Preprocessor)

Input a yap file (see doc/help.md or man yap for definition
of the yap files format) and output a nice html file.
"""

import sys
import os
import errno

from typing import Any
import argparse


# App infos
__author__ = "idealtitude"
__version__ = "0.3.0"
__license__ = "ISC"

# Constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()

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
        file_out: str | None = None
        file_in: str | None = None

        if os.path.isfile(args.file[0]):
            file_in = args.file[0]
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_in)

        if args.output:
            file_out = args.output

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
