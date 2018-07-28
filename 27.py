def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    while(count < len(nums)):
        if(nums[count] == val):
            nums.remove(val)
            continue
        count += 1
    print(nums)
    return len(nums)
print(removeElement("", [2,2],2))