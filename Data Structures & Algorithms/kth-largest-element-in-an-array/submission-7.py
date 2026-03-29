class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##Quick Select Solution
        kth = len(nums) - k
        vec = nums
        
        def quickSelect(l, r):
            if l == r:
                return vec[l]
            ppvt = l
            pivot = vec[r]

            for i in range(l, r):
                if vec[i] <= pivot:
                    vec[i], vec[ppvt] = vec[ppvt], vec[i]
                    ppvt+=1

            vec[r] = vec[ppvt]
            vec[ppvt] = pivot

            if ppvt == kth:
                return vec[ppvt]
            elif ppvt < kth:
                return quickSelect(ppvt+1, r)
            else:
                return quickSelect(l, ppvt-1)
                

        return quickSelect(0, len(nums)-1)

            
            