#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string if i != 'c' and i != 'C']
    # this join function takes all items and join them together
    return(''.join(new_string))
    # return (my_string.translate({ord(i): None for i in 'cC'}))
