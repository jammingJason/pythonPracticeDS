def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    bol_contains = True
    for number in str(num2):
        if str(num1).__contains__(str(number)):
            pass
        else:
            return False
    for num in str(num1):
        if str(num2).__contains__(str(num)):
            pass
        else:
            return False
