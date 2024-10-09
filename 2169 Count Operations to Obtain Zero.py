# https://leetcode.com/problems/count-operations-to-obtain-zero/description/
# 09/10/2024

class Solution(object):
    def countOperations(num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        while (num1 and num2):
            if num1 >= num2:
                count = count + 1
                num1 = num1 - num2
            else:
                count = count + 1
                num2 = num2 - num1
                
        return count

print (Solution.countOperations(0,0))