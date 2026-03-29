class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)] #Array of Tuples
        pairs.sort()
        stack = []

        for pair in pairs[::-1]:
            position = pair[0]
            speed = pair[1]
            time = (target-position)/speed
            stack.append(time)            
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)