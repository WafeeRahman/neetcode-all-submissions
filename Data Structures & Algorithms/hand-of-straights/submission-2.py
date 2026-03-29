#Given an array of numbers in a hnand where hand[i] is the value of the ith ccard and an int group size
#Can we resort the cards into groups of length groupSize where the values are consecutive?
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        count = {}
        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i], 0) + 1
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        total = 0
        while minHeap:
            start = minHeap[0] #Smallest Num in Sequence
            for i in range(start, start+groupSize):
                print(i, count,minHeap)
                
                if i not in count:
                    return False
                
                if count[i] == 0 and i != start:
                    return False
        
                count[i] -= 1
              
                if count[i] == 0 and i == minHeap[0]:  
                    heapq.heappop(minHeap)
  
            
            
            
        return True

   
        
        
    
        
            


        
        
        