# https://leetcode.com/problems/palindrome-number/description/
# 10/10/2024

class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        original=x
        num = 0
        # Mientras original tenga números
        while original>0:
            # Se le añade espacio al número y se le agrega el último número de original
            num = (num*10) + (original%10)
            # Se le quita el último número a original
            original = original//10

        return num == x

print (Solution.isPalindrome(8))