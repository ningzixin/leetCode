class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = []
        sum = 0
        for i in nums:
            if i not in ll:
                sum += i
                ll.append(i)
            else:
                sum -= i
        return  sum
Solution().singleNumber([4,1,2,1,2])
