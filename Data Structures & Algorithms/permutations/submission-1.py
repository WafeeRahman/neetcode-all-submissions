class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for perm in perms:
            for slot in range(len(perm)+1):
                pcopy = perm[:]
                pcopy.insert(slot, nums[0])
                res.append(pcopy)

        return res