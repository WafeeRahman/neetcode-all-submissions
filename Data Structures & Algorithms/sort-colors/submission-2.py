class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countMap = {0:0, 1:0, 2:0}

        for num in nums:
            countMap[num] += 1
        
        j = 0
        for i in range(len(nums)):
            while countMap[j] == 0:
                j+=1
           
            nums[i] = j
            countMap[j] -= 1
        

