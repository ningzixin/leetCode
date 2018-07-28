
def removeDuplicates(self, nums):
    count = 0
    while count + 1 < len(nums):
        if(nums[count] == nums[count+1]):
            nums.pop(count)
            continue
        count += 1;
    return nums

print(removeDuplicates("",[1,1]))