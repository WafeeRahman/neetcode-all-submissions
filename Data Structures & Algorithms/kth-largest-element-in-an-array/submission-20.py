import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums)-k
        def quickselect(l,r):
            if l==r:
                return nums[l]
            
            pivot = random.randint(l,r)
            nums[r], nums[pivot] = nums[pivot], nums[r]
            ppvt = l
            pivot = r
            
            for i in range(l,r):
                if nums[i] <= nums[pivot]:
                    nums[ppvt], nums[i] = nums[i], nums[ppvt]
                    ppvt+=1
            
            nums[ppvt], nums[pivot] = nums[pivot], nums[ppvt]

            if ppvt == kth:
                return nums[ppvt]
            if kth > ppvt:
                return quickselect(ppvt+1,r)
            if kth < ppvt:
                return quickselect(l, ppvt-1)
        
        return quickselect(0, len(nums)-1)