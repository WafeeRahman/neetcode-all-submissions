class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A, B = B,A
        


        l = 0 
        r = len(A)
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:

            mid = (l+r) // 2 
            mid2 = half-mid

            leftA= A[mid-1]  if mid-1 >= 0 else float('-inf')
            leftB= B[mid2-1] if mid2-1 >= 0 else float('-inf')
            rightA = A[mid] if mid < len(A) else float ('inf')
            rightB = B[mid2] if mid2 < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r=mid-1
            else:
                l=mid+1

        