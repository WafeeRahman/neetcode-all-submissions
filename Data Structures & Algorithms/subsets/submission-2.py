class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
     

        res = []

    
        def dfs(i, curSet):
            if i >= len(nums):
                res.append(curSet[:])
                return 
         
            
            dfs(i+1, curSet[:])
            
          
            curSet.append(nums[i])
            dfs(i+1, curSet[:])

         
        dfs(0, [])
   
        return res

        