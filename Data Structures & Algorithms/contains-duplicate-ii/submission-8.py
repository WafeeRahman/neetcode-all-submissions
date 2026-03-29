class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        windowSet = set()

        l=0

        for r in range(len(nums)):
            while l<r-1 and abs(r-l) > k:
                windowSet.remove(nums[l])
                l+=1
            if nums[r] in windowSet and abs(r-l) <= k:
                return True
            windowSet.add(nums[r])
        return False