
class Solution:
    import collections
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Create a Sliding Window Deque of K Length, At Each Window of K Length, append the MaxVal to the result Array
        l = 0 
        vals = collections.deque([])
        maxVal = float("-infinity")
        res = []
        for r in range(len(nums)):
            windowLen = r-l+1
            
            while vals and nums[r] > nums[vals[-1]]:
                vals.pop()
            vals.append(r)
            print(vals)
            
            if windowLen == k:
                res.append(nums[vals[0]])
                l+=1
            
            if l > vals[0]:
                print(vals)
                vals.popleft()

        return res
