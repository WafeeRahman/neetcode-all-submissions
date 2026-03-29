class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if not nums: 
            return 
        countMap = defaultdict(int)
        maxFreq = nums[0]

        for num in nums:
            countMap[num] +=1
            if countMap[num] >= countMap[maxFreq]:
                maxFreq = num
            if countMap[maxFreq] > len(nums) // 2:
                return maxFreq
        return maxFreq

