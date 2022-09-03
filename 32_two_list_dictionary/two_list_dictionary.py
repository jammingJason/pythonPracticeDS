from hashlib import new
from textwrap import fill


def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    count = 0
    new_dict = {}
    fill_value = None
    for key in keys:
        if len(keys) > len(values):
            if count < len(keys) - 1:
                fill_value = values[count]
                new_dict[key] = fill_value
                count = count + 1
            else:
                fill_value = None
                new_dict[key] = fill_value
        else:
            new_dict[key] = values[count]
            count = count + 1
    return (new_dict)
