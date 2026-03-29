class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / k)
         
            print(k, time)
            
            if time > h:
                l = k+1
            
            elif time <= h:
                r = k-1 
                res = min(k, res)
        
        return res
