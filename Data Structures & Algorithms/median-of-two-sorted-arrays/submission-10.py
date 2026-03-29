class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A)-1
        half = (len(A) + len(B)) // 2

        while True:
            
            mid = (r+l)//2
            
            aLeft = A[mid] if mid >= 0 else float('-inf')
            aRight = A[mid+1] if (mid+1) < len(A) else float('inf')
            
            bLeft = B[half-mid-2] if (half-mid-2) >= 0 else float('-inf')
            bRight = B[half-mid-1] if (half-mid-1) < len(B) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                
                if (len(A) + len(B)) % 2 == 0:
                    
                    return (min(aRight, bRight) + max(bLeft, aLeft)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r=mid-1
            else:
                l=mid+1
       



        