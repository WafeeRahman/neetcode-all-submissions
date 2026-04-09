class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res =[]
        comb = []
        def dfs(i, curSum):
            if curSum >= target:
                if curSum == target:
                    res.append(comb[:])
                return
            if i >= len(nums):
                return
            
            
            comb.append(nums[i])
            dfs(i, curSum+nums[i])
            comb.pop()

            while i > 1 and nums[i] == nums[i-1]:
                i+=1
            
            dfs(i+1, curSum)

        dfs(0,0)
        return res