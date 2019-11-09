#!/usr/bin/env python3

# ================================================================================================
# stylename.py
# Copyright 2019 Christopher Simpkins
# MIT License
#
# Dependencies:
#   1) Python 3.6+ interpreter
#   2) fonttools Python library (https://github.com/fonttools/fonttools)
#         - install with `pip3 install fonttools`
#
# Usage:
#   python3 stylename.py [OPTIONS] [FONT PATH]
#
# Notes:
#   Use quotes around arguments that include spaces
# ================================================================================================

import argparse
import os
import sys

from fontTools import ttLib

__version__ = "0.1.0"


def main():
    parser = argparse.ArgumentParser(
        description="stylename.py : an OpenType name table ID 2 and 17 editing tool"
    )
    parser.add_argument("--version", action="version", version=f"stylename.py v{__version__}")
    parser.add_argument("--id2", type=str, default=None, help="nameID 2 value")
    parser.add_argument("--id17", type=str, default=None, help="nameID 17 value")
    parser.add_argument("--all", type=str, default=None, help="nameID 2 and nameID 17 value")

    args = parser.parse_args(sys.argv[1:])

    # Command line argument tests
    #  confirm that --all flag and id2/id17 flags are not used simultaneously
    if args.all and (args.id2 or args.id17):
        sys.stderr.write(f"[ERROR] The --all option cannot be used with --id2 or --id17{os.linesep}")
        sys.exit(1)

    

    


if __name__ == "__main__":
    main()