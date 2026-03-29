class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**(32-1)) # Max Negative Value for signed 32 bit
        MAX = 2**(32-1)-1 # Max positive Value for signed 32 bit

        res=0
        while (x!=0):
            digit = math.fmod(x,10)
            x = int(x / 10)
            res = (res*10) + digit
            
            if res >= MAX or res <= MIN:
                return 0

        
        return int(res)