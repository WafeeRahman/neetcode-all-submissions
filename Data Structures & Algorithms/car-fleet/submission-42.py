class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        posSpeed = []
        for pos, spd in zip(position, speed):
           posSpeed.append((pos, spd))
        
        posSpeed.sort()

        for pos, spd in posSpeed[::-1]:
            arrivalTime = (target-pos)/spd


            stack.append(arrivalTime)
            while len(stack) >= 2 and stack[len(stack)-1] <= stack[len(stack)-2]:
                stack.pop()
        return len(stack)