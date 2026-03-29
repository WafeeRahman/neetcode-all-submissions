#With a rotated sorted array, we need to find a value at O(logn) time
#A rotated sorted array is rotated 1..n times, where the amount of rotations rotate
#The final value to the beginning of the array

#To find a value in log n time, we must use binary search
#To identify whether we are getting closer to target or not, we need to find the left sorted partition of 
#The rotated array, comparing the ends of the partition to target to see if we need to search the left sorted partition
#Or the right unsorted partition
class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0 
        r = len(nums)-1

        while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
                return mid


            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid-1
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1
        return -1
              

        