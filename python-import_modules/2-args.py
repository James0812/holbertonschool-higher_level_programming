#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("Number of arguments: 0.")
    elif argc == 1:
        print("Number of argument: 1:")
    else:
        print("Number of arguments: {}:".format(argc))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
