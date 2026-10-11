class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        write = 0
        for l in range(len(nums)):
            if nums[l] != val:
                nums[write] = nums[l]
                write+=1
        return write
            

        