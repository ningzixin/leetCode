class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ll = []
        for i in range(0,numRows):
            base = [1] * (i+1)
            if i != 0:
                base = self.getBase(base,ll[i-1])
            ll.append(base)
        print(ll)
    def getBase(self,ll,ll_before):
        ll[0] = 1
        ll[len(ll)-1] = 1
        if(len(ll) > 2):
            for i in range(1,len(ll)-1):
                ll[i] = ll_before[i] + ll_before[i-1]
        return ll
Solution().generate(5)