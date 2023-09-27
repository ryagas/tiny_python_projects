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
    out_fh.write(text.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
