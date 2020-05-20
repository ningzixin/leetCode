class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(0, len(numbers)):
        #     if numbers[i] == numbers[i-1]:
        #         continue
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #         elif numbers[i] + numbers[j] > target:
        #             continue
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif  numbers[i] + numbers[j] > target:
                if numbers[(j + i)//2]>target:
                    j = (j + i) // 2
                    continue
                j -= 1
            else:
                if numbers[(j + i) // 2]<target:
                    i = (j + i) // 2
                    continue
                i += 1
print(Solution().twoSum( [5,25,75],100))