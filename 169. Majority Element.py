class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for i in nums:
            map[i] = 0
        for i in nums:
            map[i] += 1
        max = 0
        key = 0
        for i in map.keys():
            if max < map[i]:
                max = map[i]
                key = i
        return key
print(Solution().majorityElement([2,2,1,1,1,2,2]))