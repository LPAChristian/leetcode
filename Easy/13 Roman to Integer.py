# https://leetcode.com/problems/roman-to-integer/description/
# 11/10/2024

class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        # Convertir números romanos a un array
        array = list(s)
        total = 0

        for index, i in enumerate(array):
            if i == "I":
                total += 1
            elif i == "V":
                # Si es una V, y el anterior era un I, sumarle solo 4
                if array[index-1] == "I" and index != 0:
                    total -= 1
                    total += 4
                else:
                    total += 5
            elif i == "X":
                # Si es una X, y el anterior era un I, sumarle solo 9
                if array[index-1] == "I" and index != 0:
                    total -= 1
                    total += 9
                else:
                    total += 10
            elif i  == "L":
                # Si es una L, y el anterior era una X, sumarle solo 40
                if array[index-1] == "X" and index != 0:
                    total -= 10
                    total += 40
                else:
                    total += 50
            elif i == "C":
                # Si es una C, y el anterior era una X, sumarle solo 90
                if array[index-1] == "X" and index != 0:
                    total -= 10
                    total += 90
                else:
                    total += 100
            elif i == "D":
                # Si es una D, y el anterior era una C, sumarle solo 400
                if array[index-1] == "C" and index != 0:
                    total -= 100
                    total += 400
                else:
                    total += 500
            elif i == "M":
                # Si es una M, y el anterior era una C, sumarle solo 900
                if array[index-1] == "C" and index != 0:
                    total -= 100
                    total += 900
                else:
                    total += 1000


        return total
    
print (Solution.romanToInt("MMMCDXC"))
