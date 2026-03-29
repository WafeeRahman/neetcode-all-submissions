class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        maxArea = max(heights)

        for i in range(len(heights)):
            curArea = 0
            startIndex = i
            while stack and stack[-1][0] > heights[i]:
                height, index=stack.pop()
                curArea = (i-index) * height
                maxArea = max(curArea, maxArea)
                startIndex = index
            stack.append((heights[i],startIndex))

        for i in range(len(stack)):
            curArea = (len(heights)-stack[i][1]) * stack[i][0]
            maxArea = max(maxArea, curArea)
        
        return maxArea
            