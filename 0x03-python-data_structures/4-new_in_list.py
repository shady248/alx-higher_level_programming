#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new = my_list[:]

    if 0 <= idx < length:
        new[idx] = element

    return (new)
