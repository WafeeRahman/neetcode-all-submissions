#Given an array nums, return the length of the longest subsequence where each number added is strictly increased from the previous
#A subsequence is a subarray that is allowed to be non contiguous, maintaining order but allowing elements to be deleted
#[9,1,4,2,3,3,7] -> [1,2,3,7], we're allowed to exclude the 4 and the extra 3 and include only values that are strictly increasing
#We can't really do this iteratively, so we can use DFS to explore decisions of adding every ith value to the current subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, prev):
            if i >= len(nums):
                return 0
            #At each step, we can either include the ith value in the subsequence or not
            LIS = dfs(i+1, prev)  #Explore the decision where we dont add the value in the subsequence

            #If we havent set previous yet or the current value is strictly greater than the previous
            #We can explore the decision of adding the current value to the sequence
            if prev == -1 or nums[i] > nums[prev]:
                LIS = max(LIS, (1+ dfs(i+1, i))) #Explore the next option, set previous
            
            return LIS
        

        #We can optimize this solution by caching previous calls to save on repeated work

        #Our solution space is n*n+1, for every i ranging from 0 to n, and for every j in the interval
        #(-1, 0..n), storing at j+1 each time
        def memo(i, prev):
            n=len(nums)
            memoCache = [[-1] * (n+1) for i in range(n)] #-1 represents not set
            if i >= len(nums):
                return 0

            #Store each cache call in i and prev+1 to avoid prev == -1, as thats an invalid index
            if memoCache[i][prev+1] != -1:
                return memoCache[i][prev+1]
            
            #Set the LIS for the current i
            LIS = memo(i+1, prev)

            if prev == -1 or nums[i] > nums[prev]:
                LIS = max(LIS, (1+ memo(i+1,i)))
            
            memoCache[i][prev+1] = LIS
            return memoCache[i][prev+1] #Each cache call will return from depth until the maxLIS is returned to cache[0][0]
 

        #We can further optimize this solution with tabulation, through storing each solution for the ith value in a responding
        #Dynamic programming array, and using the dp array to build a solutiion with the recurrence relation
        #Motivation: to find the max LIS dynamically by building subproblems (maxLIS for each value in nums)
        #We can start from the bottom up, starting at the end of the array as the base case, since the LIS of the final element of the array
        #Is gaurunteed to be 1, with the second being 1+dp[lastindex] iff secondlast < last
        #With this, we can make an iterative solution
        def dp():
            n = len(nums)
            #The LIS for each num in the array is atleast 1
            dp = [1] * n

            for i in range(len(nums)-1, -1, -1):
                for j in range(i, len(nums)):
                    #If we find a value that can be added to i's subsequence
                    #The the LIS of i is 1+the LIS of j, the number added to the sequence
                    if nums[j] > nums[i]:
                        dp[i] = max(dp[i], 1+dp[j])
            return max(dp)
        return dp()


            


        