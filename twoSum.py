#!/usr/bin/python 

def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i,currNum in enumerate(nums):
        if currNum >= target:
            next
        else:
            j = i+1
            while j < len (nums):
                otherNum = nums[j]
                print "evaluating " + str(currNum) + "+" + str(otherNum)
                if (currNum + otherNum) == target:
                    print "found target with " + str(i) + " and " + str(j)
                    return [i,j]
                
test1 = [11, 15, 2, 7]
testTarget = 9
print twoSum(test1, testTarget)
