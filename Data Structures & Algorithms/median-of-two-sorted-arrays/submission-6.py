class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l = 0 
        r = len(A) - 1
        
        while True:
            #Attempting to find the right midpoints for the lists A and B
            i = (l+r) // 2
            j = total - half - i - 2

            print(i+1)
            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
           
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            print(Aleft, Aright, Bleft, Bright)

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))  / 2
            
            if Aleft > Bright:
                r=i-1
                
            else:
                l=i+1




