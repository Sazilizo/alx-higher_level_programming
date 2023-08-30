#!/usr/bin/python3


def weight_average(my_list=[]):
    total = 0
    weight_count = 0
    if not my_list:
        return (0)
    for score, weight in my_list:
        total += score * weight
        weight_count += weight

    if weight_count == 0:
        return 0
    return (total / weight_count)
