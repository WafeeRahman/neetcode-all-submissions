class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        currMin = float("infinity")
        while l <=r:
            if nums[l] < nums[r]:
                currMin = min(currMin, nums[l])
                break
            mid = (l+r)//2
            currMin = min(currMin, nums[mid])
            #If we are in the left sorted portion
            if nums[l] <= nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return currMin
        