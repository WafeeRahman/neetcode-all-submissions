class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res = r

        while l<=r:
            weightCap = (r+l)//2
            daysToShip = 1
            weightSum = 0
            
            for weight in weights:
              
                if (weightSum+weight) <= weightCap:
                    weightSum += weight

                else:
                    weightSum = weight
                    daysToShip += 1
    
            
            if daysToShip > days:
                l = weightCap+1
            
            elif daysToShip <= days:
                res = min(weightCap, res)
                r = weightCap-1
                
        return res


                

