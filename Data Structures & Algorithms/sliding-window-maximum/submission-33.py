class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() #Store Indexes
        l=0
        for r in range(len(nums)):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if r-l+1 == k:
                output.append(nums[q[0]])
            print (output)
            
            while r-l+1 >= k:
                if l >= q[0]:
                    q.popleft()
                l+=1
        return output