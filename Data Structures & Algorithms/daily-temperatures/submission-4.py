class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        i = 0
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                windowlen = i-stack[-1]
                res[stack[-1]] = windowlen
                stack.pop()
            
            stack.append(i)
        return res
        