class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
     
        def backtrack(i, curSum):
            nonlocal res
            if i >= len(nums):
                res.append(curSum)
                return
            
            backtrack(i+1, curSum^nums[i])
            backtrack(i+1, curSum)
        backtrack(0,0)

        return sum(res)
            
            
            
        