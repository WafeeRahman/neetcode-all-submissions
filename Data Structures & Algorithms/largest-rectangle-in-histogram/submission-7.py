class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        stack = [] #Store Pairs of Indexes and According heightss
        maxArea = 0
        
        for i in range(len(heights)):

            startIndex = i

            while stack and stack[-1][1] > heights[i]:
                area = (i- stack[-1][0]) * stack[-1][-1]
                maxArea = max(area, maxArea)
                startIndex = stack[-1][0]
                stack.pop()

            stack.append((startIndex, heights[i]))
        
        for pair in stack:
            area = (len(heights) - pair[0]) * pair[1]
            maxArea = max(maxArea, area)
        
        return maxArea