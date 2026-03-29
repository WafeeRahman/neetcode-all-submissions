#As we iterate, we can track the values in a set with O(1) lookup, if we find a duplicate return false
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True #There is a duplicate
            
            numSet.add(num)
        #If we finish and theres no dups, retn False, theres no duplicate
        return False
         