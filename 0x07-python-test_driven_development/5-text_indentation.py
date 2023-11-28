#!/usr/bin/python3

def text_indentation(text):

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
