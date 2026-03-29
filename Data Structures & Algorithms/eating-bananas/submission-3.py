class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        #Binary Search to find the answer, which is the value k at which we can eat all bananas in minimum hours
    
        res = r #We can eat the max bananas each time and it would take h amount of hours
        while l <= r:
            
            k = (l + r) // 2
            hourCount = 0
            
            for p in piles:
                hourCount += math.ceil(p / k) #Integer division = hours it will take to consume pile p
                print(hourCount, k, p)
            
            #Binary Search
            #If our hourcount is more than hours, that means its taking us too long to eat our bananas, our min value has to increase
            if hourCount > h:
                l=k+1
            
            #If our hourcount is less, we have a valid solution, but should still look for a lesser value, decrement r
            elif hourCount <= h:
                res = min(res, k)
                r=k-1
        
        return res


        