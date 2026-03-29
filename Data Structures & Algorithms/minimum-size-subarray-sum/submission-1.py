class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        curSum = 0
        minLen = float('inf')
        for r in range(len(nums)):
            curSum += nums[r]

            while curSum >= target:
                minLen = min(minLen, (r-l+1))
                curSum -= nums[l]
                l+=1
        
        return 0 if minLen == float('inf') else minLen
        