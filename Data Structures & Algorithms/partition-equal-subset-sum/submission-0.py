#With an array of positive integers nums, partition the entire array into two halves / subsets where the sum of each
#Half is equal to one another

#[1,2,3,4] can be partitioned into two subsets [2,3] and [1,4] where both sums equal 5
#At each i we have the decision to add ith value to the subset or not

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i, curSum, otherSum):
            half = len(nums) // 2
            if i >= len(nums):
                if curSum == otherSum:
                    return True
                return False
            
            #Decide to not include to the current num
            res = dfs(i+1,curSum, otherSum+nums[i])
            if not res:
                res = res or dfs(i+1, curSum+nums[i], otherSum)
            return res
        return dfs(0,0,0)


            


        