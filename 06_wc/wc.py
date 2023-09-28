#!/usr/bin/env python3
"""
Author : Ryan Campbell <me@ryancampbell.name>
Date   : 2023-09-27
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file(s)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_bytes = 0

    total_lines, total_bytes, total_words = 0, 0, 0

    for fh in args.file:
        num_lines, num_bytes, num_words = 0, 0, 0
        for line in fh:
            num_words += len(line.split())
            num_lines += 1
            num_bytes += len(line)
        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


# TODO:
# By default, wc will print all the columns like our program does, but it will also accept flags to print -c for number of characters, -l for number of lines, and -w for number of words. When any of these flags are present, only columns for the specified flags are shown, so wc.py -wc would show just the columns for words and characters. Add short and long flags for these options to your program so that it behaves exactly like wc.
# Write your own implementation of other system tools like cat (to print the contents of a file to STDOUT), head (to print just the first n lines of a file), tail (to print the last n lines of a file), and tac (to print the lines of a file in reverse order).

# --------------------------------------------------
if __name__ == "__main__":
    main()
