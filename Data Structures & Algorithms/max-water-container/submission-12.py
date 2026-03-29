class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curArea = 0
        maxArea = float('-inf')

        l = 0 
        r = len(heights)-1

        while l < r:
            curArea = (r-l) * min(heights[l], heights[r])
            maxArea = max(curArea, maxArea)
            
            #Traverse Right PTR if its ever less than or equal to 
            #Height at left ptr
            if heights[r] <= heights[l]:
                r-=1

            #Traverse left if its ever less than right
            if heights[l] < heights[r]:
                l+=1

        return maxArea