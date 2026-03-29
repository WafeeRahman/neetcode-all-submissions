#Given an array of nums and a window size of k, there is a fixed sized of k sliding window that slides from the left of the array
#To the Right,
#Return an array of the max of each window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #Keep track of the maximum within each window of size k within nums
        #W/ Sliding Window Technique
        q = deque() #Enqueue the maximum value that we encounter in each window
        res = []
        l = 0
        maxHeap = []
        for r in range(len(nums)):
            heapq.heappush(maxHeap, [-nums[r], r])

            if len(maxHeap) >= k:
                while maxHeap[0][1] <= r-k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        
          
              
        return res
            


        
        
        
            


            


        