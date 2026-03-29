class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        nums=arr
        l=0
        r=len(nums)-1

        while r-l+1>k:
            if abs(x-nums[l]) <= abs(x-nums[r]):
                r-=1
            else:
                l+=1
        return nums[l:r+1]



        """
        l = 0
        r = len(arr)-k

        while l < r:
            mid = (r+l)//2

            if (x-arr[mid]) <= (arr[mid+k]-x):
                r = mid
            else:
                l=mid+1
        
        return arr[l:l+k]
        """