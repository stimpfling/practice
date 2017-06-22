#!/usr/bin/python

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] != val:
                nums[start] = nums[end]
                start +=1
            end +=1
        return start

soln = Solution()

nums = [3,3,2,2,3,2]
val = 3
print nums[:soln.removeElement(nums,val)]
