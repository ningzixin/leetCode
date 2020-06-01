class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import time
        import math
        start = time.time()

        n = n - 1
        era = [0] * (n+1)
        for i in range(2,n):
            if era[i] != 1:
                for j in range(i * i ,n + 1,i):
                    if j <= n:
                        era[j] = 1
                    else:
                        break
            if i * i >n:
                break
        count = 0
        for i in range(2,len(era)):
            if era[i] == 0:
                print(i)
                count += 1

        end = time.time()
        print(end - start)
        return count
print(Solution().countPrimes(10))