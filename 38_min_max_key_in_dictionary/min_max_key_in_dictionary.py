from codecs import strict_errors
from stat import ST_NLINK


def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    int_low = 0
    int_high = 0
    new_list = sorted(d.keys())
    int_low = new_list[0]
    new_list.reverse()
    int_high = new_list[0]
    print(int_low, int_high)
