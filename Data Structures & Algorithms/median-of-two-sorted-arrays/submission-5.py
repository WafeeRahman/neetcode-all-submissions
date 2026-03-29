class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Run Binary Search on the Shorter Array
        #Motivation: To find the left sorted partition of each array
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 

        #Work on the shorter array, as the longer array will probably have larger values on the right

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1 

        while True:
            #Take mid
            i = (l + r) // 2
            #Half is likely to be the left partition of b, which is the half of the totals - mid -2, (lenA) lenB
            j = half - i -2

            #Left will always be a smaller number, right will be a larger number, in case we have any invalid values
            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            #If the number at mid, the left partition of A is <= the first number in the right partition of B
            #And the number at the end of the left partition of B is less than the first number in the rightt partition,
            #We have found the correct left partition.
            if Aleft <= Bright and Bleft <= Aright:
            #If we have an odd total length, we take the minimum between first number in each right part 
                if total % 2: 
                    return min(Aright, Bright)
                #OTWS we need to find the average between the max left, and min right. (Sorted when Merged)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            #If we havent found the correct left partition between the two arrays
            #If the last number in the left partition of A is greater than the first number in the right partition of B
            elif Aleft > Bright:
                r = i - 1 #Search the left of A
            
            #If the first number in the right part of B is greater than the last part of left A, search the right of A
            else:
                l = i + 1
