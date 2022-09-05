def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    count = 0
    int_sum = 0
    total = 0
    for length in range(0, len(nums)):
        # print(nums[0])
        if len(nums) > 0 and len(nums) >= 3:
            for num in nums:
                if count < 3:
                    total = total + num
                    count += 1
            # print(total)
            int_sum = int_sum + total
            total = 0
            count = 0
            nums.remove(nums[0])
    if int_sum % 2 == 0:
        print(int_sum)
        return False
    else:
        print(int_sum)
        return True
    # print(total)
