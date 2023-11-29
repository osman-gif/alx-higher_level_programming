#!/usr/bin/python3
""" This module defines function that prints
a text with 2 new lines after 
each of these characters: ., ? and :"""


def text_indentation(text):
    """ This function that prints a text with 2 
    new lines after each of these characters: ., ? and """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for i in text:

        if i in ".?:":
            print(i, end="")
            print("")
            print("")
        else:
            print(i, end="")
