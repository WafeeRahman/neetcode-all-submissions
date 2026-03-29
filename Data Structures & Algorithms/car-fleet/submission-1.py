class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p,s in zip(position, speed)] #Array of Tuples from p[i-n] s[i-n]

        for p,s in sorted(pair)[::-1]: #Reverse Sorted Array
            stack.append((target-p)/s)
            #If the time of the newest car in the stack is smaller than the time than prev, that 
            #Indicates that they will meet at target as a fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)