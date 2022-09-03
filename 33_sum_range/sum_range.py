def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    total = 0
    count = 0
    if start > 0 and end == None:
        for num in nums:
            if count >= start:
                total = total + num
            count = count + 1
    elif start == 0 and end != None:
        for num in nums:
            if count < end + 1:
                total = total + num
                # print(total)
                count = count + 1
    elif start > 0 and end != None:
        for num in nums:
            if count >= start and count <= end:
                total = total + num
                count = count + 1
            else:
                count = count + 1
    else:
        for num in nums:
            total = total + num
    return total
