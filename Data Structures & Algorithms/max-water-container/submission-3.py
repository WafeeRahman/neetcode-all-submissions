class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        #Two Pointers
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                print(heights[l], heights[r])
                return res
        return res
