class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxHeightRight = 0
        maxHeightLeft = 0
        area = 0
        while l <= r:
            lft = height[l]
            rgt = height[r]
            maxHeightLeft = max(maxHeightLeft, lft)
            maxHeightRight = max(maxHeightRight, rgt)
            maxHeight = min(maxHeightLeft, maxHeightRight)
            areaFillable = (maxHeight - height[l]) if (maxHeight - height[l]) > 0 else 0 
            areaFillable += (maxHeight - height[r]) if (maxHeight - height[r]) > 0 else 0 
            area += areaFillable

            if height[l] >= height[r]:
                r-=1
            if height[l] < height[r]:
                l+=1
        return area



            

        