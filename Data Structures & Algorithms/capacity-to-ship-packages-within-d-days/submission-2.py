class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res = r
        while l <= r:
            mid = (r+l)//2
            daySum = 0
            dayCount = 1
            for weight in weights:
                if daySum+weight <= mid:
                    daySum+=weight
                else:
                    dayCount += 1
                    daySum = weight
            if dayCount > days:
                l = mid+1
            elif dayCount <= days:
                res = min(res,mid)
                r=mid-1
        return res
