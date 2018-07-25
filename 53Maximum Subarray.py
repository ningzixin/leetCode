class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = [] # 状态 记录以当前字符结尾的子串的最大数
        ll = nums
        i = 1
        maxNum = nums[0]
        while i < len(nums):
            if(ll[i-1]<=0):
                ll[i] = nums[i]
            else:
                ll[i] = nums[i-1] + nums[i]
            maxNum = max(ll[i],maxNum)
            i += 1
        return maxNum
print(Solution.maxSubArray("",[-2,1,-3,4,-1,2,1,-5,4]))