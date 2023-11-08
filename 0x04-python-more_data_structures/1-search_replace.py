#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if my_list is None or search is None or replace is None:
        return None
    new = my_list[:]
    idx = new.index(search, 0, len(new))

    for i in new:
        if i == search:
            idx = new.index(search, 0, len(new))
            del new[idx]
            new.insert(idx, replace)
    return (new)
