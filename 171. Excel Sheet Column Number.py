class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        x = len(s)
        sum = 0
        for i in s:
            sum += math.pow(26,x-1) * (ord(i)-64)
            x -= 1
        return int(sum)
# print(ord("A"))
print(Solution().titleToNumber("ZY"))
