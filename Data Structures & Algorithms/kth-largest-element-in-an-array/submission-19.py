import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        k=len(nums)-k
        def quickSelect(l,r):
            if l == r:
                return nums[l]
            ppvt = l
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            pivot = r
            for i in range(l,r):
                if nums[i] <= nums[pivot]:
                    nums[ppvt], nums[i] = nums[i], nums[ppvt]
                    ppvt += 1
            nums[ppvt], nums[pivot] = nums[pivot], nums[ppvt]

            if ppvt == k:
                return nums[ppvt]
            if ppvt > k:
                return quickSelect(l, ppvt-1)
            elif ppvt < k:
                return quickSelect(ppvt+1, r)
        return quickSelect(0, len(nums)-1)