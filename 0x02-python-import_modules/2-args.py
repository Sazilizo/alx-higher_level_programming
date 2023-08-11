#!/usr/bin/python3


import sys
if __name__ == "__main__":
    import sys

    argNum = len(sys.argv) - 1
    if argNum == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argNum))
    for i in range(argNum):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
