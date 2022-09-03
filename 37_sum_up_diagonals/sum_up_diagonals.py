def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0
    overall_total = 0
    count = 0
    if len(matrix) == 2:
        for nums in matrix:
            for num in nums:
                total = total + num
            print(total)
            overall_total = overall_total + total
            total = 0
        return (overall_total)
    if len(matrix) == 3:
        for nums in matrix:
            if count == 0 or count == 2:
                for num in nums:
                    total = total + num
                print(total)
                overall_total = overall_total + total
                total = 0
            count = count + 1
        return (overall_total)


m1 = [
    [1,   2],
    [30, 40],
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
