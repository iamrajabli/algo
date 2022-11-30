nums = [1, 2, 3, 9, 0, 4, 5, 8, 9]

# 1
def contains_dublicate(nums):
    return len(nums) != len(set(nums))

print(contains_dublicate(nums))

# 2
def contains_dublicate(nums):
    count = 0
    length = len(nums)
    for i in range(length):
        for k in range(length):
            if (nums[i] == nums[k]):
                count += 1

    return count != length


print(contains_dublicate(nums))
