class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            #Traversal
            #Nums[l] <= Nums[mid] indicates that we are in the left sorted portion of the array.
            if nums[l] <= nums[mid]:
                #If the number at mid is less than target, then we should check the right.
                #If the number at the left pointer is greater than the target, than we should check right
                #In each case, it tells us that the largest value in the left smaller than target, or the leftmost value is smaller than target, meaning
                #Target is in the right sorted portion
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                #If not, then that tells us that target is between l and mid, so we check the left.
                else:
                    r = mid-1
            else:
                #If we are not in the left sorted portion, we are in the right.
                #If our middle value is greater than target, than that tells us that the target lies in the left
                if nums[mid] > target or target > nums[r]:    
                    r = mid -1
                else:
                    l = mid+1
   
        return -1
            