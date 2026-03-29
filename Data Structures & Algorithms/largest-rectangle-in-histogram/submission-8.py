class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []


        for i in range(len(heights)):
            startIndex = i
            
            #Once we find a bar thats less than the one at the top of the stack, we need to take the area
            #Since we cannot continue at the height from the top of the stack
            while stack and stack[-1][1] >= heights[i]:
                #Take the Area
                currArea = (i - stack[-1][0]) * stack[-1][1]
                maxArea = max(maxArea, currArea)
                startIndex = stack[-1][0]
                stack.pop()

            stack.append((startIndex, heights[i]))

        for i in range(len(stack)):
            maxArea = max(maxArea, ((len(heights) - stack[i][0]) * stack[i][1]))
        return maxArea
