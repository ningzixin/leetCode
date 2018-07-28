class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ll = s.split(' ')
        i = len(ll)-1
        while i>=0:
            if(len(ll[i])!=0):
                return len(ll[i])
            else:
                i -= 1
        return 0
print(Solution.lengthOfLastWord("","  "))