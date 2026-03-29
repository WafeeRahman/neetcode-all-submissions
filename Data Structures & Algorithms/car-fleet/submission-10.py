class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posSpeed = [(p,s) for p, s in zip(position, speed)]
        posSpeed.sort()
        posSpeed.reverse()
        stack = []

        for speedTuple in posSpeed:
            p, s = speedTuple[0], speedTuple[1]
            time = (target-p)/s
            stack.append(time)
            print(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            



        

        