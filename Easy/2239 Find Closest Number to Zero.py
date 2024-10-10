# https://leetcode.com/problems/find-closest-number-to-zero/description/
# 09/10/2024

class Solution(object):
    def findClosestNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        contenedor = max(nums)

        for i in range(len(nums)):
            
            if nums[i] >= contenedor:
              
                if abs(nums[i]) == abs(contenedor):
                    contenedor = nums[i]
                    
                elif abs(nums[i]) < abs(contenedor):
                    contenedor = nums[i]

            elif abs(nums[i]) != abs(contenedor) and abs(nums[i]) < abs(contenedor):
                contenedor = nums[i]
                
        return contenedor
                
print (Solution.findClosestNumber([-100000,-100000]))
print (Solution.findClosestNumber([-4,-2,1,4,8]))
print (Solution.findClosestNumber([2,-1,1]))