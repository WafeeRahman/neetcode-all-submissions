class Solution:
    def canJump(self, nums: List[int]) -> bool:


        #for i..n
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, nums[i] + i)
           
        return max_reach >= len(nums)-1


        