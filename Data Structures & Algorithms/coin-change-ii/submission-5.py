class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memoC = {}

        coins.sort()

        def memo(i, curAmt):
            if curAmt > amount or i>= len(coins):
                return 0
            elif curAmt == amount:
                return 1
            elif (i, curAmt) in memoC:
                return memoC[(i, curAmt)]

            #At each step, we need to add either of the coins
            #Add current coin
            memoC[(i, curAmt)] = memo(i, curAmt+coins[i])
        

            #Move onto next, skip current coin
            memoC[(i, curAmt)] += memo(i+1, curAmt)
            return memoC[(i, curAmt)]
        return memo(0,0)