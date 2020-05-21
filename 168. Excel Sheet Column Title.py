class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n != 0:
            if n%26 == 0:
                s += "Z"
                n -= 26
            else:
                s += chr(n % 26 + 64)
            n = n // 26
        return s[::-1]
# print(Solution().convertToTitle(52))
# print(chr(65))
for i in range(26 * 26 * 26 ,26 * 26 * 26 * 26+ 10):
    print(Solution().convertToTitle(i))