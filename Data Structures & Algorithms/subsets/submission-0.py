class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            
            #Tree 1, if we included the item at index
            dfs(i+1)
            
            subset.pop()
            
            #Tree 2, if didnt include item at index
            dfs(i+1)
        
        dfs(0)    
        return res

