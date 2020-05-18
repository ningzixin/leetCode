class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ll = [0] * len(nums)
        count = 0
        for i in nums:
            if i != 0:
                ll[count] = i
                count += 1
        return ll

print(Solution().moveZeroes([0,1,0,3,12]))