class Solution:
    def reverseBits(self, n: int) -> int:
        newN = 0
        position = 0
        for i in range(32):
            bit = n & 1
            newN <<=1
            newN |= bit
            position += 1
            n >>= 1
        return newN
        