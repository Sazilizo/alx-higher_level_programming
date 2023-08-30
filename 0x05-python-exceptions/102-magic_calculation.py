#!/usr/bin/python3


def magic_calculation(a, b):
    results = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                results += a ** b / i
        except:
            results = b + a
            break
    return (results)
