class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # keep track of fleets
        posSpeed = [(p, s) for p, s in zip(position, speed)]
        posSpeed = sorted(posSpeed)

        #Reverse the list to find the cars closest to target
        for posSpeedTuple in posSpeed[::-1]:
            #Take the time of each car and compare adjacently, if
            p, s = posSpeedTuple[0], posSpeedTuple[1]
            time = (target - p) / s
            print(time)
            stack.append(time) #Add Time to Stack
            #If the newest time (ETA) added to the stack is less than the preceding value, it will be added to the fleet
            #Therefore pop it
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)
