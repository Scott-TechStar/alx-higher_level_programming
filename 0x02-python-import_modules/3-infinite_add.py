#!/usr/bin/python3
# File: 3-infinite_add.py
# John Mwadime <johnniekips@gmail.com>

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
