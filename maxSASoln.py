#!/usr/bin/python 

def maxSubArray(nums):
    if not nums:
        return 0
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num,curSum + num)
        print "curSum = " +str(curSum)
        print "maxsum = " + str(maxSum)
        print "num = " + str(num)
        print "checking max of " + str(num) +" and " + str(curSum+num)
        print
        maxSum = max(maxSum,curSum)
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [20,-15, -5, 20, 1, 1]
#nums = [8,-19,5,-4,20]
#nums = [-1]
print maxSubArray(nums)
