class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque([])
        l = 0
        res = []
        for r in range(len(nums)):
    
            
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            
            window.append(r)

            if window and window[0] < l:
                window.popleft()
            
            if r-l+1 == k:
                res.append(nums[window[0]])
                l+=1
                        
            
           

            
    
        return res
        