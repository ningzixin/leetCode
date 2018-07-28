class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #状态
        ll = []
        i = 0
        while i<n:
            i+=1
            if(i == 1):
                ll.append(1)
                continue
            if(i==2):
                ll.append(2)
                continue
            ll.append(ll[i-2]+ll[i-3])

        return ll[n-1]
print(Solution.climbStairs("",0))