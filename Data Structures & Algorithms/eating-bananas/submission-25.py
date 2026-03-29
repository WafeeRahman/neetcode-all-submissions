class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        minK = r

        while l <= r:

            k = (l+r)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil((piles[i] / k))
   
            if hours > h:
                l = k+1
            elif hours <= h:
                minK = min(minK,k)
                r=k-1
        return minK
            
        