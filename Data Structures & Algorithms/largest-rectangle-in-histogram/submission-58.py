class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #StartIndex, Height, pop when we find a height that the current value can fit underneath
        maxArea = 0
        for i, h in enumerate(heights):
            startIndex = i
            #When we encounter a height thats less than whats at the top of stack
            #That means we cannot extend the current height anymore, compute maxArea
            while len(stack) >= 1 and h < stack[-1][1]:
                stackIndex, stackHeight = stack.pop()
                curArea = (i - stackIndex) * stackHeight
                print(curArea, heights[startIndex], heights[stackIndex], startIndex, stackIndex+1)
                maxArea = max(maxArea, curArea)
                #Since the encountered height can fit under the topStackHeight,
                #We can take its starting index
                startIndex = stackIndex
                
            stack.append((startIndex, h))
        print(stack)
        while stack:
            stackIndex, stackHeight = stack.pop()
            curArea = (len(heights) - stackIndex) * stackHeight
            maxArea = max(maxArea, curArea)
        return maxArea


        