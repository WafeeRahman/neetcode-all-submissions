class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        currTriplet = triplets[0]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if currTriplet == target:
                return True
            
            currTriplet = [max(t[0], currTriplet[0]), max(t[1], currTriplet[1]), max(t[2], currTriplet[2])]
        
        return currTriplet == target
        