class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        r = len(nums)-1

        for l in range(len(nums)):
            while r >= 0 and nums[r] == val:
                r -= 1
            if l <= r and nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
        return r+1
            

        