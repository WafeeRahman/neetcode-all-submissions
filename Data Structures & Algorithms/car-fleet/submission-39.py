class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posSpeed = [(p, s) for p, s in zip(position, speed)]
        posSpeed.sort()
        posSpeed.reverse()

        stack = []

        for i in range(len(posSpeed)):
            ETA = (target-posSpeed[i][0])/posSpeed[i][1]
            while stack and stack[-1] >= ETA:
                ETA = max(ETA, stack.pop())
            stack.append(ETA)
        return len(stack)

        