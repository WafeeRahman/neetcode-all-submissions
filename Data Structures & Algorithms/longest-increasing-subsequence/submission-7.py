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
            return memoCache[i][prev+1]
        return memo(0, -1)


            


        