#!/usr/bin/python
def removeDups(nums):
    i = 0
    newLen = len(nums)
    while i < newLen:
        while newLen > i+1 and nums [i] == nums[i+1]:
            newLen -= 1
            shiftToEnd(i+1,nums,newLen)
        i+=1
    print newLen
    return nums[:newLen]

def shiftToEnd(i,nums,newLen):
    while i < newLen:
        nums[i] = nums[i+1]
        i+=1
def removeDups2(nums):
    if not nums:
        return 0 
    newTail = 0
    for i in range(1, len(nums)):
        print nums[i]
        print nums[newTail]
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]
    return newTail + 1
nums = [1,2,3,4,5]

ans= removeDups2(nums)
print ans
print nums[:ans]

