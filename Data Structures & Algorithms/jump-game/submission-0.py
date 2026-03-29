class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def greedy(i):
            n = len(nums) -1
            if i >= n:
                if i == n:
                    return True
                return False
            if nums[i] == 0:
                return False

            #Greedy, if we can atleast jump to n-1, that is a feasible solution
            #For the amount of jumplengths we can make
            
            for j in range(nums[i], 0, -1):    
                #If its feasible to jump to a position thats not beyond our bounds, test for dfs
                if (i+j) <= n and greedy(i+j):
                    return True
            return False
        return greedy(0)
                    


        