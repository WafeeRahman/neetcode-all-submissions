class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        l = 0 
        window = deque([])
        res = []
        for r in range(len(nums)):

            while window and nums[window[-1]] < nums[r]:
                window.pop()
            
            window.append(r)

            if (r-l+1) == k:
                res.append(nums[window[0]])
                l+=1
            
            if l > window[0]:
                window.popleft()
        return res
