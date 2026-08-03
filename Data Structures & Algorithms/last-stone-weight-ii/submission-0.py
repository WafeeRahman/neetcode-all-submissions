class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memoC = {}
        total = sum(stones)
        half = total // 2
        def memo(i, curSum):
            if curSum >= half or i >= len(stones):
                return abs(total - 2*curSum)
            if (i, curSum) in memoC:
                return memoC[(i,curSum)]
            

            memoC[(i, curSum)] = min(memo(i+1, curSum+stones[i]), memo(i+1, curSum))

            return memoC[(i, curSum)]

        return memo(0,0)

            