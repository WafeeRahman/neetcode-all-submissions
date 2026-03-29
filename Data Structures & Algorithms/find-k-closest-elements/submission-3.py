class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k

        while l < r:
            mid = (r+l)//2

            if (x-arr[mid]) <= (arr[mid+k]-x):
                r = mid
            else:
                l=mid+1
        
        return arr[l:l+k]