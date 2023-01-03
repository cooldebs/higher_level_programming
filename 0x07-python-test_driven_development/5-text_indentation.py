#!/usr/bin/python3
"""The "5-text_indentation module
Function:  text_indentation(text)
"""


def text_indentation(text):
    """ prints a text with 2 new lines after \
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_list = list(text)
    text_list.append("xz")
    i = 0

    while text_list[i] is not "xz":
        if text_list[i] in ['.', '?', ':']:
            while text_list[i + 1] == " ":
                text_list.pop(i + 1)
            while text_list[i - 1] == " ":
                text_list.pop(i - 1)
                i -= 1
            text_list.insert(i + 1, '\n')
            text_list.insert(i + 2, '\n')
            i += 1
        i += 1

    text_list.pop()
    for i in text_list:
        print(i, end="")
