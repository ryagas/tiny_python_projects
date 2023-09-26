#!/usr/bin/env python3
"""
Author : Ryan Campbell <me@ryancampbell.name>
Date   : 2023-09-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.str
    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    print("".join([jumper.get(char, char) for char in str_arg]))


# TODO:
# Try creating a similar program that encodes the numbers with strings (for example, “5” becomes “five,” “7” becomes “seven”). Be sure to write the necessary tests in test.py to check your work!
# What happens if you feed the output of the program back into itself? For example, if you run ./jump.py 12345, you should get 98760. If you run ./jump.py 98760, do you recover the original numbers? This is called round-tripping, and it’s a common operation with algorithms that encode and decode text.

# --------------------------------------------------
if __name__ == "__main__":
    main()
