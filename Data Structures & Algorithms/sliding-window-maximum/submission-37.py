class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        res = []
        window = deque()
        curMax = float('-inf')
        maxInd = -1
        for r in range(len(nums)):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)
            
            windowLen = r-l+1
            while windowLen == k:
                res.append(nums[window[0]])
                if l >= window[0]:
                    window.popleft()
                l+=1
                windowLen = r-l+1
        return res

        

