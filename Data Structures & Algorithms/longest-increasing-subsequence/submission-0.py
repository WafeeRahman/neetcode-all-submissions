#With an integer array nums, we need to find the length of the longest subarray
#Where each value is greater than the last while maintaining the original order of the array

#We have to maintain order so no sorting
#We cant really use iteration without having to exclude and delete values in place
#We can use two parameterred DFS to find the longest subsequence starting at a point i, traversing i deeper while storing
#The previous value in a param to check if the subsequence is increasing

#At each step we have two decisions, include the ith value in the subsequence or not based on if nums[i] is greater than the previous
#Value in the subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        def dfs(i, j):
            if i >= len(nums):
                return 0
            
            res = dfs(i+1, j)
            
            if j == -1 or nums[i] > nums[j]:
                res = max((1 + dfs(i+1, i)), res)
            
            return res
        return dfs(0, -1)



    
            

        


            



            
        