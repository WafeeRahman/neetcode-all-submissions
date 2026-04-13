class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]
        
        perms = self.permute(nums[1:])

        res = []
        for p in perms:
            for slot in range(len(p) + 1):
                pcopy = p[:]
                pcopy.insert(slot, nums[0])
                res.append(pcopy)
        return res