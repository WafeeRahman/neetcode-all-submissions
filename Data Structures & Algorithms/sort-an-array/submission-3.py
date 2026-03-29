class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def mergeSort(lst):
            if len(lst) <= 1:
                return lst

            mid = len(lst) // 2
            
            return merge(mergeSort(lst[:mid]), mergeSort(lst[mid:]))
            


        def merge(l1, l2):

            i1 = 0
            i2 = 0
            nl = []

            while i2 < len(l2) and i1 < len(l1):
                if l1[i1] < l2[i2]:
                    nl.append(l1[i1])
                    i1+=1
                else:
                    nl.append(l2[i2])
                    i2+=1
            
            if i1 < len(l1):
                for i in range(i1, len(l1)):
                    nl.append(l1[i])
            elif i2 < len(l2):
                for i in range(i2, len(l2)):
                    nl.append(l2[i])

            return nl

        return mergeSort(nums)


            
        