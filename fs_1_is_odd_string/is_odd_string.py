def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:

        >>> is_odd_string('amazing')
        True
    """
    count = 0
    for char in word:
        count = count + letters.get(char)
    if count % 2 == 0:
        return False
    else:
        return True


letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}
# Hint: you may find the ord() function useful here
