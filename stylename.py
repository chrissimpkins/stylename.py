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
#   Enter `python3 stylename.py --help` for a list of available options
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
    parser.add_argument(
        "--version", action="version", version=f"stylename.py v{__version__}"
    )
    parser.add_argument("--id2", type=str, default=None, help="nameID 2 value")
    parser.add_argument("--id17", type=str, default=None, help="nameID 17 value")
    parser.add_argument(
        "--all", type=str, default=None, help="nameID 2 and nameID 17 value"
    )
    parser.add_argument("FONT", help="Font file path")

    args = parser.parse_args(sys.argv[1:])

    # Command line argument tests
    #  confirm that --all flag and id2/id17 flags are not used simultaneously
    if args.all and (args.id2 or args.id17):
        sys.stderr.write(
            f"[ERROR] The --all option cannot be used with --id2 or --id17{os.linesep}"
        )
        sys.exit(1)

    # File path checks
    if not file_exists(args.FONT):
        sys.stderr.write(
            f"[ERROR] The font path '{args.FONT}' does not appear to exist.{os.linesep}"
        )
        sys.exit(1)

    tt = ttLib.TTFont(args.FONT)
    namerecord_list = tt["name"].names

    name_id_2 = ""
    name_id_17 = ""

    # define name ID 2 and ID 17 with command line argument definitions
    if args.id2:
        name_id_2 = args.id2
    elif args.all:
        name_id_2 = args.all
    else:
        name_id_2 = None

    if args.id17:
        name_id_17 = args.id17
    elif args.all:
        name_id_17 = args.all
    else:
        name_id_17 = None

    # edit name ID 2 and 17 records
    name_id2_updated = False
    name_id17_updated = False
    for record in namerecord_list:
        if record.nameID == 2:
            if name_id_2:
                record.string = name_id_2
                name_id2_updated = True
        if record.nameID == 17:
            if name_id_17:
                record.string = name_id_17
                name_id17_updated = True

    # write changes to the font file
    try:
        tt.save(args.FONT)
        if name_id2_updated:
            print(f"[OK] Updated '{args.FONT}' nameID 2 to '{name_id_2}'.")
        if name_id17_updated:
            print(f"[OK] Updated '{args.FONT}' nameID 17 to '{name_id_17}'.")
    except Exception as e:
        sys.stderr.write(
            f"[ERROR] Unable to edit OpenType name table for '{args.FONT}'.{os.linesep}"
        )
        sys.stderr.write(f"{e}{os.linesep}")
        sys.exit(1)


# Utilities


def file_exists(filepath):
    """Tests for existence of a file on the string filepath"""
    return os.path.exists(filepath) and os.path.isfile(filepath)


if __name__ == "__main__":
    main()
