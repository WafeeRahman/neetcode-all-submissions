class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #With an array nums and a certain integer val, remove all occurrences of val from the array
        #In place
        #Return k such that the first k elements of the array do not contain val
        #We can do this using a pivot method, where we swap val elements with non val elements
        #Ensuring that one part of the array is the unwanted elements, and the other are the elements we want to keep


        pivot = 0
        k = len(nums)

        for i in range(len(nums)):
            #Each time
            if nums[i] == val:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
                k-=1

        nums.reverse()
        return k
        

        