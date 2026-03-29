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
        for r in range(len(nums)):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            print(q)


            while (r-l)+1 >= k:
                if l > q[0]:
                    maxOfCurWindow = q.popleft()
                res.append(nums[q[0]])
                l+=1
                print(res,q)
        return res
            


        
        
        
            


            


        