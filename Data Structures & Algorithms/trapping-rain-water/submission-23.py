class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        maxHeightLeft = 0 
        maxHeightRight = 0

        while l < r:
            #Take the Max Height for Left and Right
            maxHeightLeft = max(maxHeightLeft, height[l])
            maxHeightRight = max(maxHeightRight, height[r])

            #Max Height is the minimum of max Left and max Right
            maxHeight = min(maxHeightLeft, maxHeightRight)
            print(height[l], height[r])
            print(maxHeightLeft, maxHeightRight)
            #Increment/Decrement Pointers Based on the Minimum of Left and Right
            if maxHeightLeft > maxHeightRight:
                r -= 1
                res += (maxHeight - height[r]) if ((maxHeight - height[r] > 0)) else 0
            elif maxHeightLeft <= maxHeightRight:
                l += 1
                res += (maxHeight - height[l]) if ((maxHeight - height[l] > 0)) else 0
            
        return res


            
