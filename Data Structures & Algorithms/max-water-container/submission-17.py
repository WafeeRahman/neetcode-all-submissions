class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0

        r = len(heights)-1

        maxArea = float("-inf")
        curArea=0
        while l < r:
            maxThres = min(heights[l], heights[r])
            curArea = (r-l) *maxThres
            maxArea = max(maxArea, curArea)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
            
        return maxArea