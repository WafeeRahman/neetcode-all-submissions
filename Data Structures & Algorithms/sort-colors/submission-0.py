class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        i = 0
        for j in range(3):
            while j in counts and counts[j] != 0:
                nums[i] = j
                counts[j] -= 1
                i += 1
        
            


           
