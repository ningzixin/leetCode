class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n != 0:
            if n%26 == 0 and n//26 ==1:
                s += "Z"
                n = n // 26
            else:
                s += chr(n % 26 + 64)
            n = n //26
        return s[::-1]
print(Solution().convertToTitle(51))
# print(chr(65))