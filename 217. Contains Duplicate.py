class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ll = {}
        for i in nums:
            try:
               if ll[i] == 0:
                   return True
            except:
                ll[i] = 0
        return False
print(Solution().containsDuplicate( [1,2,3,1]))
