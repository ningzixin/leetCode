import math
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if (x > math.pow(2, 31) - 1 or x < -1 * math.pow(2, 31)):
        return 0
    strH = str(x)
    if (strH[0] == '-'):
        strA = strH[1:]
        try:
            strS = '-' + strA[::-1].lstrip('0')
            if (int(strS) > math.pow(2, 31) - 1 or int(strS) < -1 * math.pow(2, 31)):
                return 0
            else:
                return eval(strS)
        except Exception as ex:
            return 0
    else:
        try:
            strS = strH[::-1].lstrip('0')
            if (int(strS) > math.pow(2, 31) - 1 or int(strS) < -1 * math.pow(2, 31)):
                return 0
            else:
                return eval(strS)
        except Exception as ex:
            return 0
print(reverse(2,213124124124))