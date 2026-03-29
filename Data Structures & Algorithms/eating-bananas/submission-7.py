class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res = r
        while l <= r:   
            k = (l+r)//2
            hourCount = 0
            
            for pile in piles:
                hourCount += math.ceil(pile / k)
            
            if hourCount > h:
                l=k+1
            elif hourCount <= h:
                res = min(res, k)
                r = k-1
        
        return res



        