class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        strA = "1"
        while i <= n:
            if(i == 1):
                strA =  "1"
            else:
                strA = Solution.getStringNum(self,strA)
            i += 1
        return strA


    def getStringNum(self,strX):
        j = 0
        ll = []
        count = 0
        while j < len(strX):
            if(len(ll)!=0 and strX[j] == ll[len(ll)-1]):
                ll[len(ll)-2] += 1
                j += 1
                continue
            ll.append(1)
            ll.append(strX[j])
            j+=1
        strA = ""
        for i in ll:
            strA  += str(i)
        return strA

print(Solution.countAndSay("",4))

