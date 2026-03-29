class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = 0
        mid = (l+r) //2
        while l <= r:
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid-1           
            else:
                return mid
            print(nums[mid])
            mid = (l+r) //2
        return -1