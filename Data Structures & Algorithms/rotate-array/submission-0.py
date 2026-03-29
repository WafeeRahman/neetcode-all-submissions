class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k%n
        if k == 0:
            return 
        
       
        l = 0
        r = len(nums)-1

        while k > 0:
            tmp = nums[r]
            for i in range(n):
                tmp2 = nums[i]
                nums[i] = tmp
                tmp = tmp2

            k -=1
        