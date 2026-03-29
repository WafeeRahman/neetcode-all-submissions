class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #Store Pairs of Indexes and According Heights
        maxArea = 0
        
        for i in range(len(heights)):
            #When we encounter a height thats less then the top of the stack
            #Take the bar's index, as the new height is less than it.
            #Meaning that the area can go under the preceding bar
            startIndex = i
            while stack and stack[-1][1] > heights[i]:
                width = i - stack[-1][0] 
                area = stack[-1][1] * width #If the next v
                maxArea = max(maxArea, area)
                startIndex = stack[-1][0]
                stack.pop()
            stack.append([startIndex, heights[i]])
        
        for i, h in stack:
                maxArea = max(maxArea, h*(len(heights) - i))

        print(stack)
        return maxArea
        