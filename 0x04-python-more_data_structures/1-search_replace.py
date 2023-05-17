#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in my_list:
        new_list = my_list.copy()
        if new_list[i] == search:
            new_list[i] = replace
        return new_list
