#Given an integer array of coins, and an integer amount, return the amount of combinations of coins that add up to amount
#Each combination must be distinct
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        def dfs(i, curSum):
            res = 0
            if curSum >= amount:
                if curSum > amount:
                    return 0
                return 1
            
            #We have the option to choose each of the coins at each step of the combination
            for j in range(i, len(coins)):
                res += dfs(j, curSum+coins[j])
            return res


        memoCache = defaultdict(int)
        def memo(i, curSum):
            res = 0
            if curSum >= amount:
                if curSum > amount:
                    return 0
                return 1
            
            if (i, curSum) in memoCache:
                return memoCache[(i, curSum)]
            
            for j in range(i, len(coins)):
                memoCache[(i, curSum)] += memo(j, curSum+coins[j])
            return memoCache[(i, curSum)]
        return memo(0,0)
        
