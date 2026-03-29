class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        res = float("infinity")

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
                
            mid = (l+r) // 2
            
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[l]: #Mid > Left tells us we're closer to the point of rotation, so search right.
                l = mid+1
            else: #If not, our minimum is closer to the right
                r = mid-1
        return res
        