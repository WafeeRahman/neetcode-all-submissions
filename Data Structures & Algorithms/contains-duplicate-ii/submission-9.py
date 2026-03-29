class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurSet = set()



        l=0
        for r in range(len(nums)):
            while abs(r-l) > k:
                occurSet.remove(nums[l])
                l+=1
            if nums[r] in occurSet and abs(r-l) <= k:
                return True
            occurSet.add(nums[r])
        return False