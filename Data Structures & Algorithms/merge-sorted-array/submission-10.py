class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        numCopy = nums1[:]


        i = 0
        j = 0
        idx = 0

        while i < m and j < n:

            if j>=n or (i < m and numCopy[i] <= nums2[j]):
                nums1[idx] = numCopy[i]
                i+=1
            elif j<n and i<m and numCopy[i] > nums2[j]:
                nums1[idx] = nums2[j]
                j+=1    
            idx+=1
        
        while j<n:
            nums1[idx] = nums2[j]
            j+=1
            idx+=1
        while i<m:
            nums1[idx] = numCopy[i]
            i+=1
            idx+=1
        




