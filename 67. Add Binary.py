class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return bin((int(a, 2)+int(b,2)))[2:]
print(Solution.addBinary("","0","0"))