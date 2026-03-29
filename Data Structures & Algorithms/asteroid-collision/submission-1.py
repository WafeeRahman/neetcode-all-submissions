class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        i=0
        stack = []
        while i < len(asteroids):
         
            while i<len(asteroids) and stack and (stack[-1] > 0 and asteroids[i] < 0):
    
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    i+=1
                elif abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                else:
                    i+=1
            if i < len(asteroids):
                stack.append(asteroids[i])
            i+=1
       
        return stack


        