class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            mid = (r+l) // 2
            subArrCount = 1
            subSum = 0
            for i in range(len(nums)):
                if subSum+nums[i] <= mid:
                    subSum += nums[i]
                else:
                    subSum = nums[i]
                    subArrCount += 1
            if subArrCount > k:
                l=mid+1
            
            elif subArrCount <= k:
                r=mid-1
                res = min(res,mid)
        
        return res