#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    results = 0
    for i in range(0, list_length):
        try:
            results = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by Zero")
            results = 0
        except TypeError:
            print("wrong type")
            results = 0
        except IndexError:
            print("out of range")
            results = 0
        finally:
            res_list.append(results)
    return (res_list)
