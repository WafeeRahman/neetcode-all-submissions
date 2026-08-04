class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memoC = {}
        def memo(i, curSum):
            if i >= len(nums):
                if curSum == target:
                    return 1
                return 0
            elif (i, curSum) in memoC:
                return memoC[(i, curSum)]
            
            #add +ve 
            memoC[(i, curSum)] = memo(i+1, curSum+nums[i])

            memoC[(i, curSum)] += memo(i+1, curSum-nums[i])    

            return memoC[(i,curSum)]
        return memo(0, 0)
        