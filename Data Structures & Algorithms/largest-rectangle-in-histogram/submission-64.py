class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        startIndex = 0
        maxArea = 0
        for i in range(len(heights)):
            startIndex = i
            #cutoff
            while stack and stack[-1][1] > heights[i]:
                j, height = stack.pop()
                maxArea = max(maxArea, (i-j)*height)
                startIndex = j
            stack.append((startIndex, heights[i]))
        

        while stack:
            j, height = stack.pop()
            maxArea = max(maxArea, (len(heights)-j)*height)
        return maxArea
            