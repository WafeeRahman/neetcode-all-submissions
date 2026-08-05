class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memoC = {}
 

        def memo(left, right):
            if left == right:
                return piles[right]
            if (left, right) in memoC:
                return memoC[(left, right)]
            
            takeLeft = piles[left] - memo(left+1, right)
            takeRight = piles[right] - memo(left, right-1)

            memoC[(left, right)] = max(takeLeft, takeRight)
            return memoC[(left, right)]

        alice = memo(0, len(piles)-1)
    

        return alice > 0

            
        