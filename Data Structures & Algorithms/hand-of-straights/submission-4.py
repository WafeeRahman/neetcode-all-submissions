#Given an array of numbers in a hnand where hand[i] is the value of the ith ccard and an int group size
#Can we resort the cards into groups of length groupSize where the values are consecutive?
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        count = {}
        #Count the amount of cards we have in the hand per value
        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i], 0) + 1
        #Sort each distinct card by its value in a minheap
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
    
        #With this minHeap, we start at the smallest value, creating consecutive groups starting at the smallest value
        #And ending at the smallest value + groupsize-1 (valid consecutive group by card value)
        while minHeap:
            start = minHeap[0] #Smallest Num in Sequence
            #The nums in the sequence should be start - start+groupsize
            #Create Group, decrement counts of associated cards we have available
            for i in range(start, start+groupSize):
                print(i, count,minHeap)
                #If the value was not in hand. we cant complete the group
                if i not in count:
                    return False
                #If we cant get the card because we have none to add to the group
                if count[i] == 0 and i != start:
                    return False
        
                count[i] -= 1

                #If we have no more values left of i and i was the smallest value, pop the minheap
                #As we cannot start at that value again
                if count[i] == 0 and i == minHeap[0]:  
                    heapq.heappop(minHeap)
  
            
            
            
        return True

   
        
        
    
        
            


        
        
        