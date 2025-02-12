def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    # populate a dictionary (hashmap) with nums as keys and index as their value
    for i in range(n):
        numMap[nums[i]] = i

    # finding the pair
    for i in range(n):
        complement = target - nums[i]  # the number added to current num in list needed for the target
        if complement in numMap and numMap[complement] != i:  # check exists and isnt the num already in use
            return [i, numMap[complement]]  # return the indices of the nums

    return []  # no solution


# Leetcode test cases
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([-1, -2, -3, -4, -5], -8))
