class Solution:
    def trap(self, height: List[int]) -> int:
        
        #Sum up the amount of water we can trap
        res = 0
        l = 0
        r = len(height) - 1
        maxHeightLeft = 0 
        maxHeightRight = 0

        while l < r:
            # Take the Max Height for Left and Right, and the min between them, which is the 
            # max amount of water we can fill
            maxHeightLeft = max(maxHeightLeft, height[l])
            maxHeightRight = max(maxHeightRight, height[r])
            maxHeight = min(maxHeightLeft, maxHeightRight)
            
            #Increment/Decrement Pointers Based on the Minimum of Left and Right
            if maxHeightLeft > maxHeightRight:
            
                #If we move the right pointer, then we check if its less than the max height
                #Between left and right (difference is non negative), that means we can fill with water
                r -= 1
                res += (maxHeight - height[r]) if ((maxHeight - height[r] > 0)) else 0
            
            elif maxHeightLeft <= maxHeightRight:

                #If we move the left pointer, then we check if its less than the max height
                #Between left and right (difference is non negative), that means we can fill with water
                l += 1
                print(maxHeight, maxHeightLeft, maxHeightRight, height[l], res)
                res += (maxHeight - height[l]) if ((maxHeight - height[l] > 0)) else 0
            
        return res


            
