class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        r = len(nums)-1
        l = 0
        swaps = 0
        while l <= r:
            while r >= 0 and nums[r] == val:
                r -= 1
            if l < r and nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]  
            l+=1
       

        return r+1
                
        
  