class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leftmain = [0] * (len(prices))
        min = 99999999
        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]
            leftmain[i] = min
        print(leftmain)
        max = 0
        for i in range(1,len(prices)):
            if (prices[i] - leftmain[i]) > max:
                max = prices[i] - leftmain[i]
        return max
print(Solution().maxProfit([7,1,5,3,6,4]))