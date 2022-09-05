def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    dict_vowels = []
    str_s = s
    count = 0
    for char in s:
        for vow in vowels:
            if count < len(str_s):
                str_s = (str_s.replace(vow, '!'))
                count += 1
            if vow == char:
                dict_vowels.append(char)
    dict_vowels.reverse()

    count = 0
    new_str = str_s
    for char in s:
        for vow in dict_vowels:
            if count < len(str_s):
                new_str = (new_str.replace("!", vow, 1))
                count += 1
            # if vow == char:
            #     dict_vowels.append(char)
    return (new_str)
