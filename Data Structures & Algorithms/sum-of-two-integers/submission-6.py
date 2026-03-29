class Solution:
    def getSum(self, a: int, b: int) -> int:
        #Since python has an ulimited amount of bits, we need to use bit masks to maintain a 32 bit integer limit
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while (b!=0):
            tmp = (a & b) << 1
            a = (a^b) & mask
            b = tmp & mask
        return a if a <= max_int else ~(a^mask)

       
