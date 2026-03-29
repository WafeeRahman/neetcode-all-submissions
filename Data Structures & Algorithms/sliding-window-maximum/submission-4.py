
class Solution:
    import collections
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0 
        vals = collections.deque([])
        maxVal = float("-infinity")
        res = []
        for r in range(len(nums)):
            windowLen = r-l+1
            vals.append(nums[r])
            if windowLen == k:
                print(l, r)
                print (vals)
                maxVal = max(vals)
                res.append(maxVal)
                vals.popleft()
                l+= 1
        return res
