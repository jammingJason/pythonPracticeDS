def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    new_dict = {}
    new_phrase = phrase.lower()
    
    for char in new_phrase:
        for letter in 'aeiou':
            if char == letter:
                new_dict[char] = new_phrase.count(char)
    print (new_dict)