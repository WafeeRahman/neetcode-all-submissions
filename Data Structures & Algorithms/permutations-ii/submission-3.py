class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curPerm = []
        used = set()
        def backtrack(slot):
            if len(curPerm) == len(nums):
                res.append(curPerm[:])
                return
     
            

            for i in range(len(nums)):
                if i in used:
                    continue
                if i >= 1 and nums[i] == nums[i-1] and not (i-1) in used:
                    continue
                used.add(i)
                curPerm.append(nums[i])
                backtrack(i+1)

                curPerm.pop()
                used.remove(i)
    
        backtrack(0)
        return res