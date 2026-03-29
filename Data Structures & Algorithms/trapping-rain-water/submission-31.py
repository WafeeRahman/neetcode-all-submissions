class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r=len(height)-1
        maxHeightLeft = 0
        maxHeightRight = 0

        res = 0
        while l < r:
            maxHeightLeft = max(height[l], maxHeightLeft)
            maxHeightRight = max(height[r], maxHeightRight)
            thres = min(maxHeightLeft, maxHeightRight)
            
           
            if height[l] <= height[r]:
                res += (thres - height[l]) if (thres-height[l]) > 0 else 0
                l+=1
                
            else:
            
                res += (thres - height[r]) if (thres-height[r]) > 0 else 0
                r-=1
                
        return res


