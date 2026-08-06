class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        memoC = {}


        def memo(alice, i, M):
            if i >= len(piles):
                return 0
            elif (alice, i, M) in memoC:
                return memoC[(alice, i, M)]
            
            res = 0 if alice else float('inf')
          
            curSum = 0
            for x in range(1, 2*M +1):
                if i+x > len(piles):
                    break
                curSum += piles[i+x-1]
    
                if alice:
                    #Max Alice
                    res = max(res, curSum+memo(not alice, i+x, max(M, x)))
                else:
                    #Minimize Bob's
                    res = min(res, memo(not alice, i+x, max(M, x)))

            memoC[(alice, i, M)] = res
            
            return memoC[(alice, i, M)]
        return memo(True, 0, 1)
            