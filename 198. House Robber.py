class Solution(object):
    def f(self, nums, n):
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0]+nums[2],nums[1])
        else:
            return self.f(nums[0:-3],n-3) + max(nums[n-1]+nums[n-3],nums[n-2])
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.f(nums, len(nums))
print(Solution().rob([2,7,9,3,1]))
