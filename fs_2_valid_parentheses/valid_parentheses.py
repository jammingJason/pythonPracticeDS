def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    list(parens)
    count_left = 0
    count_right = 0
    for p in parens:
        if p == '(':
            count_left += 1
        elif p == ')':
            count_right += 1
    if parens[0] != '(':
        return False
    elif len(parens) % 2 != 0:
        return False
    elif count_left != count_right:
        return False
    else:
        return True
