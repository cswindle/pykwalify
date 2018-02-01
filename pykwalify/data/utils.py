def merge(d1, d2):
    """ Merges two dictionaries together.
        Updates d1 in place and returns it"""

    if not d1:
        d1 = {}

    if not d2:
        d2 = {}

    # iterate over all the keys in d1 and add to the
    for k in d1.keys():
        # if k is common to both dictionaries
        if k in d2.keys():
            # if k has a dictionary as a value use this function to merge them
            if isinstance(d2[k], dict):
                d1[k] = merge(d1[k], d2[k])
            # if k has a list as value merge the list, but remove duplicates
            elif isinstance(d1[k], list):
                d1[k] = remove_duplicates(d1[k], d2[k])
            else:
                d1[k] = d2[k]
    # add all the keys to d1 that are only in d2
    for k in d2.keys():
        if k not in d1.keys():
            d1[k] = d2[k]
    # return the first dictionary, which has been updated
    return d1


def remove_duplicates(list1, list2):
    """ this function takes two lists and
        returns a list that contains all the elements
        only once"""
    array = list1 + list2
    ans = []
    found = False
    length = len(array)
    for i in range(length):
        found = False
        for j in range(i):
            if(array[i] == array[j]):
                found = True
                break
        if not found:
            ans.append(array[i])
    return ans
