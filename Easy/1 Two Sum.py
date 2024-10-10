# https://leetcode.com/problems/two-sum/description/
# 10/10/2024

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indexI, i in enumerate(nums):
            for indexN, n in enumerate(nums):
                if i+n == target and indexI != indexN:
                    return ([indexI,indexN])
    
print (Solution.twoSum([3,2,4],19999))
