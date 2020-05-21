class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # temp_b = 0
        # temp_t = 0
        # for j in range(0,k):
        #     for i in range(0,len(nums)):
        #         if(i == 0):
        #             temp_t = nums[(i+1)%len(nums)]
        #             nums[(i + 1)%len(nums)] = nums[i%len(nums)]
        #         else:
        #             temp_b = nums[(i+1)%len(nums)]
        #             nums[(i+1)%len(nums)] = temp_t
        #             temp_t = temp_b
        # return nums
        ll = [0]*len(nums)
        for i in range(0, len(nums)):
            ll[(i + k) % len(nums)] = nums[i]
        for i in range(0, len(ll)):
            nums[i] = ll[i]
        return nums
print(Solution().rotate([1,2,3,4,5],1))


