class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def backtrack(i, nums):
            #Bottom Up BackTrack Recursion, start with a list with
            #An empty permutation
            if i == len(nums):
                return [[]]
            res = []
            perms = backtrack(i+1, nums)

            for permutation in perms:
                for j in range(len(permutation) + 1):
                    pcopy = permutation[:]
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res
                    
        return backtrack(0, nums)
       

            
        
        
    
    