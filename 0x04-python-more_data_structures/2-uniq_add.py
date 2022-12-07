#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_new_list = []
    result = 0
    for i in my_list:
        if i not in my_new_list:
            my_new_list.append(i)
            result += 1
    return result
