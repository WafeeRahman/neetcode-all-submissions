class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float('inf')

        while l <= r:
            if nums[r] >= nums[l]:
                minimum = min(nums[l], minimum)
            mid = (l+r)//2
            minimum = min(nums[mid], minimum)
            #If we are in the left sorted portion, minimum is likely to be in the right
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return minimum           

