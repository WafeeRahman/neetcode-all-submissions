class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=set()
        curPerm = []
        nums.sort()
        res = []
        
        def backtrack(startIndex):
            if len(curPerm) == len(nums):
                res.append(curPerm[:])
                return
            

            for i in range(len(nums)):
                if i in used:
                    continue

                if i >= 1 and nums[i] == nums[i-1] and (i-1) not in used:
                    continue
                
                curPerm.append(nums[i])
                used.add(i) 
                backtrack(i+1)

                used.remove(i)
                curPerm.pop()
        backtrack(0)
        return res            
                
            


