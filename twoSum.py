"""
Given an array of integers, return indices of the two numbers such that they add up to a 
specific target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def sum(nums, target):
    for i in range(len(nums)):
        if(target - nums[i]) in nums[i+1:]:
            return [i, nums[i+1:].index(target - nums[i])+i+1]

def sum_anoth(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (target - nums[i] == nums[j]):
                return [i, j]

nums = [2,5,5,11]
target = 10

indecies = sum(nums, target)
print indecies

indecies = sum_anoth(nums, target)
print indecies


