class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1

        while l <= r:

            

            while l<r and nums[l] == nums[l+1]:
                l+=1
            
            while l<r and nums[r-1] == nums[r]:
                r-=1
            
            mid = (r+l) // 2

            if nums[mid] == target:
                return True

            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[r] >= nums[mid]:
                if nums[r] < target or nums[mid] > target:
                    r=mid-1
                else:
                    l=mid+1
        return False
        