class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        n = str(bin(n)[2:])
        if len(n) < 32:
            n = "0" * (32 - len(n)) + n
        sum = 0
        for i in range(0,len(n)):
            if n[i] == "1":
                sum += 1
        return sum