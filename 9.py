def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    strA = str(x)
    if(strA[::-1] == strA):
        return True
    else:
        return False


def fff(x):
    if(x<0):
        return False
    ll = []
    while(x!=0):
        ll.append(x%10)
        x = x // 10
    count = 0;
    for i in ll:
        if(i != ll[len(ll)-count-1]):
            return False
        count += 1
    return True

print(fff(122521))