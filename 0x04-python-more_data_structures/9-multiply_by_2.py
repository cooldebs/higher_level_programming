#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for value in a_dictionary:
        return [list(map(lambda x: x * 2, value))]
