class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(lst):
            if len(lst) <= 1:
                return lst
            half = len(lst) // 2

            res = mergeLists(mergeSort(lst[0:half]), mergeSort(lst[half:]))

            return res




        def mergeLists(l1, l2):
            i, j = 0,0
            nl = []

            while i < len(l1) and j < len(l2):
                print(l1[i], l2[j])
                if l1[i] < l2[j]:
                    nl.append(l1[i])
                    i+=1
                else:
                    nl.append(l2[j])
                    j+=1

            if i < len(l1):
                nl.extend(l1[i:])
            else:
                nl.extend(l2[j:])
            
            return nl
        return mergeSort(nums)