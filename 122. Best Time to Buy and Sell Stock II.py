class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #先试试贪心
        sum = 0
        min = prices[0]
        max = prices[0]
        for i in range(0,len(prices)):
            if prices[i] > max:
                max = prices[i]
            if prices[i] < min:
                min = prices[i]
                max = min
            if max > min:
                sum += max-min
                min = max
        return sum
Solution().maxProfit([7,6,4,3,1])