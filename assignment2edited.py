def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."

    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."

    # filter odd and even numbers into two separate lists
    Odd_nums = [num for num in nums if num % 2 == 1]
    Even_nums = [num for num in nums if num % 2 == 0]

    odd_nums = []
    even_nums = []




    # remove duplicates and sort
    i = 0
    for j in Odd_nums:
        l = 0
        k = i
        while len(Odd_nums) > k:
            if j == Odd_nums[k]:
                l = l + 1
            k = k + 1
        if l < 2:
            odd_nums.append(j)
        i = i + 1


    i = 0
    for j in Even_nums:
        l = 0
        k = i
        while len(Even_nums) > k:
            if j == Even_nums[k]:
                l = l + 1
            k = k + 1
        if l < 2:
            even_nums.append(j)
        i = i + 1

    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)

    return odd_nums, even_nums

nums = [20,90,50,57,50,20,19]
odd_nums, even_nums = split_and_sort(nums)

print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)
