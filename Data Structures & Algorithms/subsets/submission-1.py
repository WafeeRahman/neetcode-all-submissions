class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            #Base Case to return
            if i >= len(nums):

                res.append(subset[:])
                return
            
            #
            subset.append(nums[i])
            
            #BackTracking Recursion Tree 1, if we included the node
            dfs(i+1)
            
            #BackTracking Recursion Tree 2, if we didnt include the node
            subset.pop()
            
            dfs(i+1)

        dfs(0)
            
        return res

