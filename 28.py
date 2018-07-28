


def getNext(keyStr):
    j = 0
    k = -1
    next = [-1]
    while j < len(keyStr) - 1:
        if k == -1 or keyStr[j] == keyStr[k]:
            j += 1
            k += 1
            next.append(k)
        else:
            k = next[k]
    return next

def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    #字符串匹配 暴力解法
    # i = 0
    # j = 0
    # if(needle == None or len(needle) == 0):
    #     return 0
    # while i < len(haystack):
    #     if(i + len(needle) <= len(haystack) and haystack[i:i+len(needle)] == needle):
    #         return i
    #     i += 1
    # return -1

    # kmp算法
    next = getNext(needle)
    i = 0
    j = 0
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(needle):
        return i - j
    else:
        return -1



print(strStr("","",""))