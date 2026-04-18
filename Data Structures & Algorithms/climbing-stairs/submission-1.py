class Solution:
    def climbStairs(self, n: int) -> int:
        memoC = defaultdict(int)
        def memo(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memoC:
                return memoC[i]
            
            memoC[i] += memo(i+1)
            memoC[i] += memo(i+2)

            return memoC[i]
        memo(0)
        return memoC[0]