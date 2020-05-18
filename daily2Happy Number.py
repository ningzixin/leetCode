class Solution(object):
    def getNum(self,n):
        sum = 0
        for i in str(n):
            sum += int(i) * int(i)
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            temp = self.getNum(n)
            if temp == 1:
                return True
            else:
                n = temp
print(Solution().isHappy(19))