class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0


        r = len(nums)-1

        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l=mid+1
                else:
                    r=mid-1

            elif nums[mid] <= nums[r]:
                if nums[r] < target or nums[mid] > target:
                    r=mid-1
                else:
                    l=mid+1
                    

            
        
        return -1