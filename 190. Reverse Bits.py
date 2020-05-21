class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        import math
        n = str(bin(n)[2:])
        if len(n) < 32:
            n = "0"*(32-len(n))+n
        print(n)
        sum = 0
        for i in range(0, len(n)):
            sum += math.pow(2,i) * int(n[i])
        return int(sum)
print(Solution().reverseBits(43261596))