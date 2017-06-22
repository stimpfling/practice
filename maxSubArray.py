#!/usr/bin/python 

def maxSubArray(nums):
    if not nums:
        return 0 
    maxSum = currentSum = nums[0]
    for val in nums[1:]:
        currentSum = max(val+currentSum,val)
        maxSum = max(currentSum,maxSum)
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [8,-19,5,-4,20]
#nums = [-1]
print maxSubArray(nums)
