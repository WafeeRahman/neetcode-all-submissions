class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        used = set()
        
        target = sum(nums) // k
        nums.sort(reverse=True)
        def backtrack(start, curSum, buckets):
            nonlocal target
            if buckets > k:
                return False
            if buckets == k:
                return True
            
            if curSum == target:
                return backtrack(0, 0, buckets+1)
            
            for av in range(start, len(nums)):
                if av in used:
                    continue
                if nums[av] + curSum > target:
                    continue
                else:
                    used.add(av)
                    if backtrack(av+1, curSum+nums[av], buckets):
                        return True
                    used.remove(av)

                    if curSum == 0:
                        return False
            return False
        return backtrack(0,0,0)
            


            