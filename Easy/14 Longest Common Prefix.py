# https://leetcode.com/problems/longest-common-prefix/description/
# 11/10/2024

class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Si la lista está vacía, devolver ""
        if len(strs) == 0:
            return ""

        # Empezamos con que el prefijo sea la primera palabra entera
        prefix = strs[0]
        # Iteramos en la lista empezando por el segundo valor
        for i in strs[1:]:
           
            # Mientras que la letra no empieze por el prefijo, lo vamos acorrtando
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                #  Si ya no hay prefijo, devolver ""
                if prefix == "":
                    return prefix
        return prefix

        

print (Solution.longestCommonPrefix(["pedro","pedlovv","pedlon"]))
