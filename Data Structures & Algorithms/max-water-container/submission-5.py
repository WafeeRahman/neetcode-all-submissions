class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        #Two Pointers
        l = 0
        r = len(heights) - 1

        while l < r:

            area = min(heights[l], heights[r]) * (r-l)
            #Take the area using the minimum height

            res = max(res, area)
            #Get the max Area

            #Traverse Pointers Based On Height
            if heights[l] <= heights[r]:
                l+=1 
            elif heights[r] < heights[l]:
                r-=1
       
        return res
