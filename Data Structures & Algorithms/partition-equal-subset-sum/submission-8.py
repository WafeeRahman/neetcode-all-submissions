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
        
        #We can store every subset sum starting at the end of the list starting at the end of
        def dp():
            nonlocal total
            #If total is uneven, then it cant be split into two halves of subset sums
            if total % 2:
                return False
            #If one of the subset sums equates to half of the total, that tells us another half
            #exists within the set that adds to total
            target = total // 2
            dp = set()
            #Subset Sum of Not Including any values
            dp.add(0) 

            for i in range(len(nums)-1,-1,-1):
                #Create A new DP set as we cant add values to a set in iteration
                newDP = set()
                for num in dp:
                    #Add the subset sum, aswell as the old vals of the subset themselvs
                    newDP.add(num)
                    newDP.add(nums[i] + num)
                    if target in dp:
                        return True
                dp = newDP #Overwrite dp with the new subset sums
                
            return target in dp
        
        return dp()


            


        