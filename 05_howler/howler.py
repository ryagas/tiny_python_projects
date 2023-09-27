#!/usr/bin/env python3
"""
Author : Ryan Campbell <me@ryancampbell.name>
Date   : 2023-09-27
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input string or file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default="",
    )

    parser.add_argument("--ee", action="store_true", help="convert text to lowercase")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if outfile:
        out_fh = open(outfile, "wt")
    else:
        out_fh = sys.stdout

    if args.ee:
        out_fh.write(text.lower() + "\n")
    else:
        out_fh.write(text.upper() + "\n")
    out_fh.close()


# TODO:
# Alter the program to handle multiple input files. Change --outfile to --outdir, and write each input file to the same filename in the output directory.

# --------------------------------------------------
if __name__ == "__main__":
    main()
