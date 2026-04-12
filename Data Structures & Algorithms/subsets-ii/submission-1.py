class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
   
        res = []
        curComb = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(curComb[:])
                return
            
            
            
          
            curComb.append(nums[i])
            dfs(i+1)

           
            curComb.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return res