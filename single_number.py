nums = [2, 1, 2, 14, 0, 0, 14]

# T: O(N)
# S: O(1)
# XOR


def single_number(nums):
    result = 0
    for i in nums:
        result = result ^ i

    return result


print(single_number(nums))

