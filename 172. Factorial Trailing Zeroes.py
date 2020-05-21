class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n % 10 >= 5:
        #     print((n//10)*2 + 1)
        # else:
        #     print((n//10) * 2)\
        zeros = 0
        while n > 0:
            zeros += n // 5
            n //= 5
        return int(zeros)
print(Solution().trailingZeroes(30))

