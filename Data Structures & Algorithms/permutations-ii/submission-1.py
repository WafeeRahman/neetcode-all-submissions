class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        curPerm = []
        nums.sort()
        def backtrack(i):
      
            if len(curPerm) == len(nums):
                res.append(curPerm[:])
       


            for slot in range(len(nums)):
                if slot in used:
                    continue
                if slot >= 1 and nums[slot] == nums[slot-1] and not (slot-1) in used:
                    continue
                
                used.add(slot)
                curPerm.append(nums[slot])
                backtrack(slot+1)

                used.remove(slot)
                curPerm.pop()
              
        

        backtrack(0)
        return res