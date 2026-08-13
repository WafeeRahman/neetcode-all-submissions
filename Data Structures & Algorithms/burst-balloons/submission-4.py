class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        

        memoC = {}

        def memo(left, right):
            if (left, right) in memoC:
                return memoC[(left, right)]
            if left+1 == right:
                return 0
            

            best = 0
            for i in range(left+1, right):
                lft = nums[left]
                rght = nums[right]
                pop = nums[i] * lft * rght
                pop += memo(left, i)
                pop += memo(i, right)

                best = max(best, pop)
            memoC[(left, right)] = best
            return memoC[(left, right)]
        return memo(0, len(nums)-1)
      