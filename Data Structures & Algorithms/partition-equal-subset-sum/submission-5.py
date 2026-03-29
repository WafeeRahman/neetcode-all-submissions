#With an array of positive integers nums, partition the entire array into two halves / subsets where the sum of each
#Half is equal to one another

#[1,2,3,4] can be partitioned into two subsets [2,3] and [1,4] where both sums equal 5
#At each i we have the decision to add ith value to the subset or not

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i, curSum, otherSum):
            if i >= len(nums):
                if curSum == otherSum:
                    return True
                return False
            
            #Decide to not include to the current num
            res = dfs(i+1,curSum, otherSum+nums[i])
            if not res: #If this returns false, check the other decision to see if 
                res = res or dfs(i+1, curSum+nums[i], otherSum) #Including the current value allow for two equal partitions
            return res
   
        
        #Instead of incrementing both a curSum and otherSum, we know that the otherSum 
        #Will be the total of nums - the current sum
        total = sum(nums)
        if total%2 != 0: #We also know that if total isnt even it wont be able to be split into two equal sums
            return False
        #Memoize Previous Solutions
        cache = {}
        def memo(i, curSum):
            nonlocal total
            #ShortCut if curSum is already greater than half the total to save on memory in caache
            if i >= len(nums) or curSum >= total-curSum:
                if curSum == total-curSum:
                    return True
                return False
            #Lookup previous solutions if they exist
            if (i,curSum) in cache:
                return cache[(i,curSum)]
            #Set Solution for current i and cursum pair in cache with dfs
            res = memo(i+1, curSum) or memo(i+1, curSum+nums[i])
            cache[(i,curSum)] = res
            
            return res
        
        return memo(0,0)


            


        