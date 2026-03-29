#Given an array of nums where nums[i] equals the maximum length you can make a jump from the ith position to the i = nums[i]th poistion
#Find the minimum number of jumps to reach the last position in array n-1
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #Greedy Method, we want to take the minimum jump that will take us to arr[n]

        q = deque([(0,0)])
        visit = {}

        while q:
            print(q)
            curPos, curJumped = q.popleft()
            if curPos >= len(nums)-1:
                return curJumped
            
            visit[curPos] = curJumped
            
            #Greedy - Check for Feasible Values Starting at the minimum amount of jumps it takes to reach the next position
            for jump in range(1, nums[curPos]+1):
                if (curPos+jump) not in visit:
                    q.append((jump+curPos, curJumped+1))
        
        return -1
        


