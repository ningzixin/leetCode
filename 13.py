base = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def romanToInt(self, s):
    count = 0
    sum = 0;
    for i in s:
        count += 1
        if(count <= len(s) - 1):
            if(base[i]>=base[s[count]]):
                sum = sum + base[i]
            else:
                sum = sum - base[i]
            continue
        sum = sum + base[i]

    print(sum)
romanToInt(1,'III')