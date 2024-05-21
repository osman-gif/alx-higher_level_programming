#!/usr/bin/python3
""" This module contains a script
that adds all arguments to a Python list,
and then save them to a file """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args_list = ""
loaded_data = ""

# Add the cmd args to a list (args_list)
for i in range(1, len(sys.argv)):
    my_args = sys.argv
    args_list = args_list + " " + my_args[i]

j_file = "add_item.json"

# Checks if the file is empty, or can't load data
try:
    loaded_data = load_from_json_file(j_file)
except pass:
    # If file is empty save the args list to the
    # json file first
    save_to_json_file(args_list, j_file)
    sys.exit()
# If file not empty load it data
loaded_data = load_from_json_file(j_file)

# and then add the loaded data to the args list
# and then save them to the json file
json_file = save_to_json_file(loaded_data + args_list, j_file)
