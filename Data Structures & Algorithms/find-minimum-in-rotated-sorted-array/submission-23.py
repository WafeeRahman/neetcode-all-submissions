class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1 

        minVal = nums[l]
        while l<=r:


            mid = (l+r)//2
            minVal = min(minVal, nums[mid], nums[l], nums[r])
            if nums[l] <= nums[mid]:
                l=mid+1

            else:
                r=mid-1
        return minVal


            