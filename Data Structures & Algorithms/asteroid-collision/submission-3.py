class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        i=0
        while i < (len(asteroids)):


            while i < len(asteroids) and stack and stack[-1] > 0 and asteroids[i] < 0:

                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    i+=1
                
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()

                elif abs(stack[-1]) > abs(asteroids[i]):
                    i+=1
                    
            
            if i < len(asteroids):
                stack.append(asteroids[i])
            i+=1
        return stack

                
        