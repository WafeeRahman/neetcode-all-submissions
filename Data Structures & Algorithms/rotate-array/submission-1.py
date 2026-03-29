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
        
       
        nums.reverse()
        print(k)
        
        l = 0
        r = k-1

        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
        
            l+=1
            r-=1
        
        r=n-1
        l = k
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
        
            l+=1
            r-=1
        
