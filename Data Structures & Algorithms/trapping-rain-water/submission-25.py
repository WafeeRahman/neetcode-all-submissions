class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        maxLeft=0
        maxRight=0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            thres = min(maxLeft, maxRight)

            res += thres - height[l] if thres-height[l] > 0 else 0
            res += thres - height[r] if thres-height[r] > 0 else 0

            if height[l] < height[r]:
                l+= 1
            elif height [r] <= height[l]:
                r-=1
        return res