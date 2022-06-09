#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)


'''
def simple_delete(my_dict, key=""):
    my_dict.pop(key, None)
    return (my_dict)
'''
