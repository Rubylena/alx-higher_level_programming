#!/usr/bin/python3


def complex_delete(my_dict, value):
    dict_copy = my_dict.copy()

    for k, v in dict_copy.items():
        if value == v:
            del my_dict[k]
    return (my_dict)
