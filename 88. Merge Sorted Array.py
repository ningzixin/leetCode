class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[0:m]
        num2 = nums2[0:n]
        i= 0
        j = 0
        while j < len(num2):
            if(num2[j]>=num1[i] or i == len(num1) -1):
                num1.insert(i+1,num2[j])
                j += 1
            else:
                j += 1
        return num1
print(Solution.merge("",[1,2,3,0,0,0],3,[2,5,6],3))