#!/usr/bin/env python3
"""
Author : Ryan Campbell <me@ryancampbell.name>
Date   : 2023-09-25
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items", metavar="str", help="Item(s) to bring", nargs="+")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if len(args.items) == 1:
        print(f"You are bringing {args.items[0]}.")
    elif len(args.items) == 2:
        if args.sorted:
            args.items.sort()
        print(f"You are bringing {' and '.join(args.items)}.")
    else:
        if args.sorted:
            args.items.sort()
        last_item = args.items.pop()
        print(f"You are bringing {', '.join(args.items)}, and {last_item}.")


# TODO
# Add an option so the user can choose not to print with the Oxford comma (even though that is a morally indefensible option).
# Add an option to separate items with a character passed in by the user (like a semicolon if the list of items needs to contain commas).

# --------------------------------------------------
if __name__ == "__main__":
    main()
