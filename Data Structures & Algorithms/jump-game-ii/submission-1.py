#Given an array of nums where nums[i] equals the maximum length you can make a jump from the ith position to the i = nums[i]th poistion
#Find the minimum number of jumps to reach the last position in array n-1
class Solution:
    def jump(self, nums: List[int]) -> int:
        #Return minimum jumps req'd to reach n
        #Feasible Solution
        jumps = 0
        maxReach = 0
        i=0
        while i < len(nums):
            if i >= len(nums)-1:
                return jumps
            
            if i + nums[i] >= len(nums)-1:
                return jumps+1
            
            optimalJump = nums[i]
            maxReach = i + nums[i]
            
            #At each step, we need to choose the jump that will give us the maximum reach, which will give us
            #The minimum amount of jumps required
            #Optimal jump can be 1..nums[i]
            
            for j in range(0, nums[i]+1):
                
                #If we jump to i+j, for j in range 0..nums[i], can we reach further than i + nums[i]?
                #If we can, update the maxReach to i+j+numspi+j]
                #And our optimal jump is to add j to i and move to i+j 
                if i + j + nums[i+j] >= maxReach:
                    maxReach = i+j+nums[i+j]
                    optimalJump = j
                
        
            i+=optimalJump #jump to most optimal jump
            jumps+=1

        return jumps
        


        
