class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        res = r
        while l <= r:
            mid = (l+r)//2

            splits = 1
            curSum = 0

            for num in nums:
                if curSum+num > mid:
                    splits+=1
                    curSum=num
                else:
                    curSum += num
           

            if splits > k:
                l = mid+1
            elif splits <= k:
                res = min(res, mid)
                r = mid-1
                
            
        return res


        