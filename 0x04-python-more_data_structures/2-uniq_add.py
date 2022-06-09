#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return result


'''
def uniq_add(my_list=[]):
    return sum(set(my_list))
'''
