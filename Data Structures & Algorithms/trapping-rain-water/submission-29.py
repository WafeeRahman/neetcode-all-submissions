class Solution:
    def trap(self, height: List[int]) -> int:
        

        l = 0
        r = len(height)-1

        maxHeightLeft = float('-inf')
        maxHeightRight = float('-inf')
        res = 0
        heights = height
        while l <= r:
            maxHeightLeft = max(maxHeightLeft, height[l])
            maxHeightRight = max(maxHeightRight, height[r])
            thres = min(maxHeightLeft, maxHeightRight)
            
            if heights[l] > heights[r]:
                res += (thres - heights[r]) if (thres - heights[r]) > 0 else 0
                r-=1

            if heights[l] <= heights[r]:
                res += (thres - heights[l]) if (thres - heights[l]) > 0 else 0
                l+=1
         


        return res


            