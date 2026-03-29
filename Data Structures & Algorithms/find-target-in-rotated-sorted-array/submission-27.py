class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1


        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            #If we are in the left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
        return -1


        