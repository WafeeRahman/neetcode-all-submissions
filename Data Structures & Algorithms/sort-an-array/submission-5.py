class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l1, l2):
            i1 = 0
            i2 = 0
            nl = []
            
            #Compare and add smallest first
            while i1 < len(l1) and i2 < len(l2):
            
                item1 = l1[i1]
                item2 = l2[i2]

                if item1 < item2:
                    nl.append(item1)
                    i1+=1
                else:
                    nl.append(item2)
                    i2+=1
            
            #Once one of them finishes processing extend the rest of the elements into newlist
            if i1 < len(l1):
                for j in range(i1, len(l1)):
                    nl.append(l1[j])
            
            if i2 < len(l2):
                for j in range(i2, len(l2)):
                    nl.append(l2[j])
            
            
            return nl



        
        def mergeLists(nums):
            #Return len 1 or empty lists in splits
            if len(nums) <= 1:
                return nums
            
            #split and merge halfs
            l = mergeLists(nums[:len(nums)//2])
            r = mergeLists(nums[len(nums)//2:])
            nums = merge(l, r)
            return nums
        
        return mergeLists(nums)
        

        