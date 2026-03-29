class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionAndSpeed = []

        for i in range(len(position)):
            positionAndSpeed.append((position[i],speed[i]))
        
        positionAndSpeed.sort()
        positionAndSpeed.reverse()
   

        stack = []
        for i in range(len(positionAndSpeed)):
            print(target, positionAndSpeed[i])
            ETA = (target-positionAndSpeed[i][0])/positionAndSpeed[i][1]
            print(ETA, stack)
            
            while stack and stack[-1] >= ETA:
                ETA=max(stack.pop(), ETA)
            stack.append(ETA)
        
        print(stack)
        return len(stack)
