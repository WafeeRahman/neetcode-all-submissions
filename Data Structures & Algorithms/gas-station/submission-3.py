#There are n gas stations in a circular route
#Where given arrays gas and cost, where gas[i] is the amount of gas a the ith station, and cost is the respective cost to travel in gas
#We have a car with 0 intial gas but can start at any ith station, wcan we find a route such that we can start and return to the ith station
#By taking gas from each of the other stations?

# gas = [1,2,3,4], cost = [2,2,4,1]
#Return 3, we can start at index 3 with the most gase, travel to
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        #if this isnt true, that means that for some station, gas should accumulate enough to go clockwise
        #We need to find that station by greedily ignoring stations that will take our gas station to the negatives

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) #Net Gain
            
            #Reset Window if total is ever negative, it means we ran out of gas and therefore cannot move
            #meaning that the current station cannot be the solution
            if total < 0:
                total = 0
                res = i+1 #Check next station
        return res
                

        
        

