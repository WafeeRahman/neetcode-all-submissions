class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        buckets = [[] * k]
        used = set()
        bucketNo = 0
        nums.sort(reverse=True)
        target = sum(nums) // k
        def backtrack(startIndex, curSum, bucketsFilled):
            if bucketsFilled == k:
                return True
            
            if curSum >= target:
                if curSum == target:
                    return backtrack(0, 0, bucketsFilled+1)
                else:
                    return False 

            for i in range(startIndex, len(nums)):
                if i in used:
                    continue
                if curSum + nums[i] <= target:
                    used.add(i)
                    if backtrack(i+1, curSum+nums[i], bucketsFilled):
                        return True
                    used.remove(i)
                    if curSum == 0:
                        break
            
            return False
        
        return backtrack(0, 0, 0)


                
