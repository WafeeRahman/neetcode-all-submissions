class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k > n:
            k = k%n
        if k==0:
            return
        

        while k > 0:
            k-=1
            top = nums[-1]
            #Shift Right

            for i in range(n-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = top

        
            