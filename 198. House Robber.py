class Solution(object):
    def f(self, nums, n):
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0],nums[1])
        if n == 2:
            return max(nums[0]+nums[2],nums[1])
        else:
            return max(self.f(nums[0:-1],n-1) , self.f(nums[0:-2],n-2) + nums[n])
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[i]
print(Solution().rob([2,7,9,3,1]))
