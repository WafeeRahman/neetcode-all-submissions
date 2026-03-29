#Given an array of numbers in a hnand where hand[i] is the value of the ith ccard and an int group size
#Can we resort the cards into groups of length groupSize where the values are consecutive?
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        nums = hand.copy()
        nums.sort()
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        
        visit = set()
    
        while len(visit) != len(nums):
            i = 0 
            prev = None
            curGroup = []
            while i < len(nums):
                if len(curGroup) == groupSize:
                    break 
                if i in visit or prev and nums[i] == prev:
                    i+=1
                    continue
                if curGroup and nums[i] != curGroup[-1] +1:
                    return False
                curGroup.append(nums[i])
                visit.add(i)
                prev = nums[i]
                i+=1
            if len(curGroup) != groupSize:
                return False
        return len(visit) == len(nums)
                
            


        
        
        