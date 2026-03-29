#With an integer array of nums and an integer target, we need to find the number of ways we can sum to target
#Having choices either to add or subtract the current number to the current sum
#Add Or Subtract Knapsack, we must reach the target capacity
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        def dfs(i, curSum):
            if i == len(nums): 
                if curSum == target:
                    return 1
                return 0 
            print(curSum)
            res = 0
            res += dfs(i+1, curSum + nums[i])
            res += dfs(i+1, curSum + -(nums[i]))

            return res
     
        
        memoC = {}

        def memo(i, curSum):
            if i >= len(nums): 
                if curSum == target:
                    return 1
                return 0 
            if (i, curSum) in memoC:
                return memoC[(i, curSum)]
            
            ways = 0
            ways += memo(i+1, curSum + nums[i])
            ways += memo(i+1, curSum + -(nums[i]))
            memoC[(i, curSum)] = ways
            return memoC[(i, curSum)]
        return memo(0,0)
            


         