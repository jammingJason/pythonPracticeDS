def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = ''
    next_item = True
    for char in phrase:
        if next_item == True:
            new_phrase = new_phrase + char.upper()
        else:
            new_phrase = new_phrase + char.lower()
        if char == ' ':
            next_item = True
        else:
            next_item = False
    return (new_phrase)
