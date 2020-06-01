class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_c = {}
        if len(s) != len(t):
            return  False
        for i in range(0,len(s)):
            if s[i] not in map_c.keys() and t[i] not in map_c.values():
                map_c[s[i]] = t[i]
        tmp = ""
        for i in s:
            try:
                tmp += map_c[i]
            except:
                return False
        if tmp == t:
            return True
        return False
print(Solution().isIsomorphic("ab","aa"))