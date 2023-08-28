#!/usr/bin/python3

def safe_print_integer(value):
    is_dig = True
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
    except TypeError:
        return (False)
