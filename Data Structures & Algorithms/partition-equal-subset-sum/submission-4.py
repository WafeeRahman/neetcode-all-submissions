#With an array of positive integers nums, partition the entire array into two halves / subsets where the sum of each
#Half is equal to one another

#[1,2,3,4] can be partitioned into two subsets [2,3] and [1,4] where both sums equal 5
#At each i we have the decision to add ith value to the subset or not

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def dfs(i, curSum):
            nonlocal total
            
            if i >= len(nums):
                if curSum == total-curSum:
                    return True
                return False
            
            #Decide to not include to the current num
            res = dfs(i+1,curSum)
            if not res:
                res = res or dfs(i+1, curSum+nums[i])
            return res
        return dfs(0,0)
        

        def memo(i, curSum, otherSum):
            n = len(nums)
            memoCache = [[-1] * n+1 for i in range(n)]
            
            if i >= len(nums):
                if curSum == otherSum:
                    return True
                return False

            if memoCache[curSum][otherSum] != -1:
                return memoCache[i]
            
            memoCache[i] = memo(i+1,curSum, otherSum+nums[i])
            if not memoCache[i]:
                memoCache[i] = memoCache[i] or memo(i+1, curSum+nums[i], otherSum)
            return memoCache[i]
        return memo(0,0,0)


            


        