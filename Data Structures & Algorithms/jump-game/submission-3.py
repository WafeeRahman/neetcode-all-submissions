class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #for n-1 to 0, track if we can reach the goal, if the ith position can reach the goal, that means it itself is the goal
        #Continue this until we can verify that position zero can reach the goal
        n = len(nums)-1
        goal = n

        for i in range(n-1, -1, -1):
            if i+nums[i] >= goal:
                goal = i
            
        return goal == 0
        


        