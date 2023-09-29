#!/usr/bin/env python3
"""
Author : Ryan Campbell <me@ryancampbell.name>
Date   : 2023-09-28
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("letter", nargs="+", metavar="str", help="Letter(s)")

    parser.add_argument(
        "-f",
        "--file",
        help="Input file (default: gashlycrumb.txt)",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    line_dict = {}

    for line in args.file:
        line_dict[line[0]] = line
    for letter in args.letter:
        if letter.upper() in line_dict:
            print(line_dict[letter.upper()].strip())
        else:
            print(f'I do not know "{letter}".')


# TODO:
# Write a phonebook that reads a file and creates a dictionary from the names of your friends and their email or phone numbers.
# Create a program that uses a dictionary to count the number of times you see each word in a document.
# Write an interactive version of the program that takes input directly from the user. Use while True to set up an infinite loop and keep using the input() function to get the user’s next letter:
# $ ./gashlycrumb_interactive.py
#     Please provide a letter [! to quit]: t
#     T is for Titus who flew into bits.
#     Please provide a letter [! to quit]: 7
#     I do not know "7".
#     Please provide a letter [! to quit]: !
#     Bye
# --------------------------------------------------
if __name__ == "__main__":
    main()
