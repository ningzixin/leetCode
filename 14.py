def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    x = strs[0]
    count = 0
    for i in x:
        for j in strs:
            try:
                if(i != j[count]):
                    return x[0:count]
            except:
                return x[0:count]
        count += 1
    return x[0:count]
print(longestCommonPrefix('',[""]))

